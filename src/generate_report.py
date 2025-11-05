import pandas as pd
import json

def save_results_json(results, filename="data/results.json"):
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

def save_results_csv(results, filename="data/results.csv"):
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
