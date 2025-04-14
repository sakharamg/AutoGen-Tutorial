import json
from datetime import datetime
import pickle
from difflib import SequenceMatcher
from pathlib import Path
import random
from agents.persona_generator import PersonaGenerator, parse_personas_from_text
from agents.agent_creator import create_agents_from_personas
from core.conversation_orchestrator import run_conversation

class DirectorAgent:
    def __init__(self, llm_config, prompt_path="config/prompts.json", event_memory_path="event_memory.pkl"):
        Path("memory").mkdir(parents=True, exist_ok=True)
        self.prompt_path=prompt_path
        self.llm_config = llm_config
        self.event_memory_path = f"memory/{event_memory_path}"
        self.generated_events = self.load_event_memory()
    def is_similar_event(self, event, existing_events, threshold=0.8):
        return any(
            SequenceMatcher(None, event.lower(), ev.lower()).ratio() > threshold
            for ev in existing_events
        )
    def load_event_memory(self):
        try:
            with open(self.event_memory_path, "rb") as f:
                memory = pickle.load(f)
                print(f"Loaded {len(memory)} past events from memory.")
                return memory
        except FileNotFoundError:
            print("No memory found. Starting fresh.")
            return set()

    def save_event_memory(self):
        with open(self.event_memory_path, "wb") as f:
            pickle.dump(self.generated_events, f)
    def run(self, task_type, max_rounds=6, num_runs=1):
        print(f"\nDirectorAgent running task: {task_type} x {num_runs} times")

        for i in range(num_runs):
            self.curr_run = i + 1
            self.llm_config["cache_seed"] = random.randint(0, 1_000_000)
            self.pg = PersonaGenerator(self.prompt_path, self.llm_config)

            MAX_RETRIES = 5
            for attempt in range(MAX_RETRIES):
                avoid_list = list(self.generated_events)[-30:]  # recent 30 events
                persona_text = self.pg.generate_personas(task_type, avoid_events=avoid_list)
                self.last_persona_text = persona_text

                try:
                    personas, shared_event = parse_personas_from_text(persona_text, task_type=task_type)
                except Exception as e:
                    print(f"Parsing failed. Retrying... ({e})")
                    continue

                # Check if shared event is new
                if not self.is_similar_event(shared_event, self.generated_events):
                    self.generated_events.add(shared_event)
                    break
                else:
                    print(f"Similar event detected: \"{shared_event}\". Retrying...")

                print("Failed to generate unique event after retries. Skipping.")
                continue

            agents = create_agents_from_personas(personas, self.llm_config, shared_event, task_type=task_type)
            messages = run_conversation(agents, max_rounds=max_rounds)
            self.save_data(task_type, personas, shared_event, messages)
            self.save_event_memory()


    
    def save_data(self, task_type, personas, shared_event, messages, model="gpt-4o", save_dir="outputs"):
        data = {
            "task_type": task_type,
            "shared_event": shared_event,
            "personas": personas,
            "conversation": [
                {
                    "turn": i + 1,
                    "name": m["name"],
                    "role": m["role"],
                    "content": m["content"]
                }
                for i, m in enumerate(messages)
                # if m["role"] == "assistant"
            ],
            "metadata": {
                "model": model,
                "timestamp": datetime.now().isoformat()
            }
        }

        Path(save_dir).mkdir(exist_ok=True)
        filename = f"{task_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{self.curr_run}.json"
        filepath = Path(save_dir) / filename

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print(f"\nData saved to {filepath}")
