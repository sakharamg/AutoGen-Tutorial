from autogen.agentchat import AssistantAgent
from utils.config import get_llm_config

code_agent = AssistantAgent(
    name="CodeAgent",
    llm_config=get_llm_config(),
    system_message="You are a coder. Generate runnable Python code for the given experiment plan."
)
