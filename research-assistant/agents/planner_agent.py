from autogen.agentchat import AssistantAgent
from utils.config import get_llm_config

planner_agent = AssistantAgent(
    name="PlannerAgent",
    llm_config=get_llm_config(),
    system_message=(
        "You are a planner. Given a research topic and literature, design a clear experiment plan "
        "including models, datasets, and evaluation metrics."
    )
)
