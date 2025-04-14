from utils.config import get_llm_config
from core.director_agent import DirectorAgent

if __name__ == "__main__":
    llm_config = get_llm_config()
    director = DirectorAgent(llm_config)
    director.run("chat_between_friends", max_rounds=6, num_runs=5)
