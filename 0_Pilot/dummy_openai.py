import openai
import yaml

# Load config from YAML
with open("../config.yaml", "r") as f:
    config = yaml.safe_load(f)

api_key = config["openai"]["api_key"]
model = config["openai"].get("model", "gpt-3.5-turbo")

# Use new SDK-style client
client = openai.OpenAI(api_key=api_key)

# Make a request using the new client
response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": "Tell me a fun fact about space."}
    ]
)

print("OpenAI response:")
print(response.choices[0].message.content)
