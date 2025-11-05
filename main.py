from src.poll_models import poll_models
from src.evaluate_responses import evaluate_responses
from src.generate_report import save_results_json, save_results_csv
import yaml

def main():
    print("🚀 Welcome to modelometer! Measuring AI brilliance... 🚀")
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    
    all_results = []
    for keyword in config["keywords"]:
        print(f"\n🔍 Polling models for keyword: '{keyword}'")
        responses = poll_models(keyword)
        scores = evaluate_responses(keyword, responses)
        scores["keyword"] = keyword
        all_results.append(scores)
    
    save_results_json(all_results)
    save_results_csv(all_results)
    print("\n✅ Results saved to data/results.json and data/results.csv")
    print("🎉 modelometer analysis complete!")

if __name__ == "__main__":
    main()
