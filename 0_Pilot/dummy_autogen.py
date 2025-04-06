import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
import yaml
import os

# Load OpenAI config from YAML
with open("../config.yaml", "r") as f:
    yaml_config = yaml.safe_load(f)

# Set env var for AutoGen to pick up
os.environ["OPENAI_API_KEY"] = yaml_config["openai"]["api_key"]

async def main() -> None:
    model_client = OpenAIChatCompletionClient(model=yaml_config["openai"].get("model", "gpt-3.5-turbo"))
    agent = AssistantAgent("assistant", model_client=model_client)
    print(await agent.run(task="Say 'a fun fact about mother earth!'"))
    await model_client.close()

asyncio.run(main())