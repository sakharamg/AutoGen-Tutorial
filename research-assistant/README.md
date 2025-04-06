# 🧠 AutoGen Research Assistant (Multi-Agent)

This weekend project is a modular, multi-agent research assistant built using Microsoft's [AutoGen](https://github.com/microsoft/autogen). It combines LLM agents with tool use, planning, and code execution to automate tasks like literature review, planning, and Python coding.

---

## 🚀 Features

- **LiteratureAgent**: Uses `arxiv` tool to find relevant research papers
- **PlannerAgent**: Designs experiments given a research question
- **CodeAgent**: Generates Python code and executes it
- **UserProxyAgent**: Initiates the task, can be set to `TERMINAL` or `NEVER`
- **GroupChatManager**: Coordinates conversation between agents

---

## 🛠️ Setup

### 1. Create and activate a conda environment

```bash
conda create -n autogen-research python=3.10 -y
conda activate autogen-research
```

### 2. Install dependencies

```bash
pip install autogen[chat,tools] autogen-core autogen-agentchat autogen-ext[openai]
pip install pyyaml arxiv tiktoken
```

---

## 🔑 Configure OpenAI

Edit `config.yaml`:

```yaml
config_list:
  - model: gpt-4
    api_key: sk-your-real-openai-key-here
```

---

## 🧪 Run the Research Assistant

```bash
python main.py
```

Agents will:
1. Find relevant papers
2. Plan an experiment
3. Generate and execute code
4. Save output to: `data/results/run_output.txt`

---

## 📁 Directory Structure

```text
research-assistant/
├── agents/           # Agent definitions
├── tools/            # External tools (e.g., Arxiv search)
├── utils/            # Shared config and helper code
├── data/
│   └── results/      # Output is stored here (ignored by Git)
├── main.py           # Entry point
├── config.yaml       # Your OpenAI config
├── .gitignore
└── README.md         # This file
```

---

## 🧠 Credits & Inspirations

- [AutoGen by Microsoft](https://github.com/microsoft/autogen)
- ArXiv API via `arxiv` Python package
- Agent structure inspired by ReAct + Planner-Code loop
