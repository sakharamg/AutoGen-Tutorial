import yaml

def get_llm_config(path="config.yaml"):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    return {"config_list": config["config_list"]}
