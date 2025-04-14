import json
import re
from autogen.agentchat import AssistantAgent

class PersonaGenerator:
    def __init__(self, prompt_config_path, llm_config):
        with open(prompt_config_path, 'r') as f:
            self.prompts = json.load(f)
        self.agent = AssistantAgent(
            name="PersonaGenAgent",
            llm_config=llm_config,
            human_input_mode="NEVER"
        )

    def generate_personas(self, task_type, avoid_events=None):
        prompt = self.prompts.get(task_type)
        if not prompt:
            raise ValueError(f"No prompt found for task type: {task_type}")

        if avoid_events:
            avoid_text = "\nAvoid repeating any of these events:\n" + "\n".join(f"- {ev}" for ev in avoid_events)
            prompt += "\n" + avoid_text

        messages = [{"role": "user", "content": prompt}]
        response = self.agent.generate_reply(messages)

        if not response:
            raise ValueError("LLM returned no content.")
        return response

def parse_personas_from_text(text,task_type="chat_between_friends"):
    if task_type=="chat_between_friends":
        shared_event_match = re.search(r"Shared Event:\s*(.*)", text)
        shared_event = shared_event_match.group(1).strip() if shared_event_match else "a recent shared experience"

        persona_blocks = text.strip().split("Persona 2:" if "Persona 2:" in text else "Persona B:")
        personas = []
        for block in persona_blocks:
            name = re.search(r"Name:\s*(.+)", block)
            age = re.search(r"Age:\s*(\d+)", block)
            city = re.search(r"City:\s*(.+)", block)
            interests = re.search(r"Interests?:\s*(.+)", block)
            personality = re.search(r"Personality?:\s*(.+)", block)
            persona = {
                "name": name.group(1).strip().replace(" ","_") if name else "Agent",
                "age": age.group(1).strip() if age else "25",
                "city": city.group(1).strip() if city else "Unknown",
                "interests": interests.group(1).strip() if interests else "N/A",
                "personality": personality.group(1).strip() if personality else "N/A"
            }
            personas.append(persona)
        return personas, shared_event
    else:
        # fallback to chat parsing (already done)
        raise(f"Invalid task type: {task_type}")
