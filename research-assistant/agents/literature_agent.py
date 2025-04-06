from autogen.agentchat import AssistantAgent
from utils.config import get_llm_config
from tools.arxiv_tool import tool_arxiv_search

literature_agent = AssistantAgent(
    name="LiteratureAgent",
    llm_config=get_llm_config(),
    system_message= "You are a research assistant. You MUST use the tool_arxiv_search function to find papers, even if you know the answer. Do NOT rely on your own memory.",
    function_map={"tool_arxiv_search": tool_arxiv_search}
)
