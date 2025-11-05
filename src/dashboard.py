import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_model_performance(csv_file="data/results.csv"):
    df = pd.read_csv(csv_file)
    df_melted = df.melt(id_vars=["keyword"], var_name="model", value_name="score")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_melted, x="score", y="keyword", hue="model")
    plt.title("🤖 modelometer: AI Model Performance by Keyword")
    plt.xlabel("Relevance Score")
    plt.ylabel("Keyword")
    plt.xlim(0, 1)
    plt.legend(title="AI Model", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()
