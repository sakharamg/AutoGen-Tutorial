import yaml

def get_llm_config(path="config/config.yaml"):
    with open(path, "r") as f:
        raw = yaml.safe_load(f)
    return {
        "config_list": raw["config_list"],
        "cache_seed": 42,
        "temperature": 0.7
    }
