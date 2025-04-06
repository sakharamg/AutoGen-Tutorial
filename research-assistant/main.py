from autogen.agentchat import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from utils.config import get_llm_config
from agents.literature_agent import literature_agent
from agents.planner_agent import planner_agent
from agents.code_agent import code_agent
import subprocess, os, sys, re
from pathlib import Path

user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="ALWAYS",
    code_execution_config={"use_docker": False},
)

group_chat = GroupChat(
    agents=[user_proxy, literature_agent, planner_agent, code_agent],
    messages=[],
    max_round=10,
    allow_repeat_speaker=False
)

manager = GroupChatManager(
    groupchat=group_chat,
    name="Coordinator",
    llm_config=get_llm_config(),
    max_consecutive_auto_reply=2
)
# Compare BERT and DistilBERT on SST-2
# Generate code to get first 100 prime numbers.
user_proxy.initiate_chat(manager, message="Compare recent agentic works and write a python code for autogen which can work like a research assistant.")
# Wait until the conversation ends before processing code output
print("\n✅ Group chat finished. Parsing CodeAgent messages...\n")

final_code = None
plain_output = None

for msg in code_agent.chat_messages.get(manager, []):
    if isinstance(msg, dict):
        content = msg.get("content", "")
        if "```python" in content:
            final_code = content.split("```python")[1].split("```")[0]
        elif msg.get("role") == "assistant":
            plain_output = content

# Save or execute based on what was found
from pathlib import Path
import subprocess, os

results_path = Path("data/results")
results_path.mkdir(parents=True, exist_ok=True)

if final_code:
    print("🧠 Code block found. Executing...")
    with open(results_path / "temp_code.py", "w") as f:
        f.write(final_code)
    result = subprocess.run(["python", results_path / "temp_code.py"], capture_output=True, text=True)
    with open(results_path / "run_output.txt", "w") as f:
        f.write(f"--- STDOUT ---\n{result.stdout}\n\n--- STDERR ---\n{result.stderr}")
    print("✅ Code executed and output saved.")
elif plain_output:
    with open(results_path / "run_output.txt", "w") as f:
        f.write(f"--- PLAIN OUTPUT ---\n{plain_output}")
    print("✅ Response saved without code block.")
else:
    with open(results_path / "run_output.txt", "w") as f:
        f.write("No assistant response was generated within the allowed rounds.\n")
    print("⚠️ No assistant response found to save.")
