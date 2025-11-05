import openai
import yaml

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def poll_openai(model_name, prompt):
    api_key = load_config()["api_keys"]["openai"]
    openai.api_key = api_key
    response = openai.Completion.create(
        model=model_name,
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def poll_anthropic(model_name, prompt):
    api_key = load_config()["api_keys"]["anthropic"]
    return f"Response from {model_name} for '{prompt}'"

def poll_llama(model_name, prompt):
    api_key = load_config()["api_keys"]["llama"]
    return f"Response from {model_name} for '{prompt}'"

def poll_models(keyword):
    config = load_config()
    results = {}
    for model in config["models"]:
        if model["type"] == "openai":
            results[model["name"]] = poll_openai(model["name"], keyword)
        elif model["type"] == "anthropic":
            results[model["name"]] = poll_anthropic(model["name"], keyword)
        elif model["type"] == "llama":
            results[model["name"]] = poll_llama(model["name"], keyword)
    return results
