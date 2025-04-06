# AutoGen Tutorial 🚀

This tutorial walks you through building agentic AI systems using Microsoft's AutoGen and OpenAI. It's designed in modular stages, starting with minimal working examples (pilot) and gradually progressing toward more complex agent setups like dataset assistants and planners.

---

## 📁 Project Structure

```
autogen-tutorial/
├── 0_Pilot/               # Minimal working examples
│   ├── dummy_openai.py    # Basic OpenAI call using config.yaml
│   └── dummy_autogen.py   # Minimal AutoGen agent chat
├── research-assistant     # Multi-agent system that does literature survey, analysis, code and execute
├── config.yaml            # Stores your OpenAI API key (ignored via .gitignore)
├── requirements.txt       # Project dependencies
├── .gitignore             # Prevents secrets and unwanted files from being committed
└── README.md              # You're reading it :)
```

---

## 🧪 Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sakharamg/autogen-tutorial.git
   cd autogen-tutorial
   ```

2. **Create a Conda environment**:
   ```bash
   conda create -n autogen-env python=3.10 -y
   conda activate autogen-env
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `config.yaml`** (this is **not committed** for security):
   ```yaml
   openai:
     api_key: "sk-..."  # Your OpenAI API key
     model: "gpt-3.5-turbo"
   ```

5. **Run the pilot scripts**:
   ```bash
   cd 0_Pilot
   python dummy_openai.py
   python dummy_autogen.py
   ```

---

## 🔐 Security Notes

- Do **not** share your `config.yaml` — it contains your OpenAI secret key.
- This file is listed in `.gitignore` to avoid accidental commits.

---
## 🚧 Progress and Future Plan:

### ✅ What’s Done?
- `0_Pilot/`: Code to test that setup is done correctly
- `research-assistant/`: Multi-agent system that does literature survey, analysis, code and execute
----

### 🧱 What’s Next?


- `data_gen-assistant/`: Multi agents for generating diverse data

Stay tuned 👀

---

## 🤝 Contributions

Feel free to fork the project, create issues, or suggest features to improve this tutorial.

---

## 🧠 Author

Built with ❤️ by [Sakharam Gawade](https://www.linkedin.com/in/sakharam-gawade/) — exploring agentic AI and research-oriented tooling for real-world LLM applications.
