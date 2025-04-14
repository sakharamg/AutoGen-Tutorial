# Multi-Agent Dialogue Orchestrator

This project builds a flexible framework for simulating conversations between language agents using [AutoGen](https://github.com/microsoft/autogen). These conversations can be used for data generation, research, and prototyping agent behavior across multiple domains.

---

## ✅ Features

- Dynamic persona generation using LLMs  
- Multi-turn agent-to-agent conversations  
- Task-specific prompts (e.g., friend chats, diagnosis)  
- Conversation memory to avoid repetition (e.g., unique shared events)  
- Turn-aware dialogue with natural wrap-ups  
- Structured output saved as JSON

---

## 📦 Directory Structure

```
AutoGen-Tutorial/
├── agents/                   # Persona creation and agent initialization
├── core/                     # DirectorAgent and conversation orchestration
├── config/
│   ├── prompts.json          # Task-specific prompt templates
│   └── config.yaml           # LLM model and API key config
├── tools/                    # (reserved for future use: tool functions)
├── outputs/                  # Saved conversations
├── memories/                 # Deduplication memory per task
├── main.py                   # Entry point for running a task
└── README.md
```

---

## 🧠 How It Works

1. **DirectorAgent** orchestrates the entire pipeline  
2. **PersonaGenerator** creates unique agent personas  
3. **Agents** are initialized with these personas and system messages  
4. **Conversation loop** drives the multi-turn chat between agents  
5. **Turn manager** ensures natural, back-and-forth dialogue  
6. **Conversation + metadata** are saved to disk  

---

## ✨ Current Use Case: Chat Between Friends

### Task  
Generate a natural conversation between two friends based on their unique personas and a shared event.

### Example Output

```json
{
  "task_type": "chat_between_friends",
  "shared_event": "They attended a music festival in Austin...",
  "personas": [
    { "name": "Alex", "age": 28, "interests": "photography" },
    { "name": "Jamie", "age": 26, "interests": "reading" }
  ],
  "conversation": [
    { "turn": 1, "name": "Alex", "content": "Hey Jamie! Remember that music fest?" },
    { "turn": 2, "name": "Jamie", "content": "Of course! Still thinking about those tacos." }
  ],
  "metadata": {
    "model": "gpt-4o",
    "timestamp": "2025-04-13T22:12:00"
  }
}
```

### Deduplication Strategy

To ensure novelty across runs, we:
- Store previously generated events in memory (RAM + disk)
- Pass recent events to the LLM prompt to avoid
- Retry generation if similar event is detected (via fuzzy matching)