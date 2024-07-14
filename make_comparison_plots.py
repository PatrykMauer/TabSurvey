import json
import matplotlib.pyplot as plt
import numpy as np

# Load model results from JSON file
with open('output/all_results.json') as f:
    models = json.load(f)

# Datasets and their corresponding file names
datasets = [
    {"name": "AuctionResultsNoImg", "file_suffix": "dataset1"},
    {"name": "CaliforniaHousing", "file_suffix": "dataset2"},
    {"name": "AuctionResultsColor", "file_suffix": "dataset3"},
    {"name": "AuctionResultsColorSVD", "file_suffix": "dataset4"},
    {"name": "AuctionResultsSVD", "file_suffix": "dataset5"}
]

# Desired order of methods
method_order = [
    "LinearModel", "KNN", "DecisionTree", "RandomForest", "XGBoost", "CatBoost",
    "LightGBM", "MLP", "TabNet", "VIME", "TabTransformer", "ModelTree",
    "DeepGBM", "RLN", "DNFNet", "NAM", "DeepFM", "SAINT"
]

bar_width = 0.35

def sort_methods(data, methods, order):
    order_map = {method: idx for idx, method in enumerate(order)}
    sorted_data = sorted(zip(methods, *data), key=lambda x: order_map.get(x[0], float('inf')))
    return list(zip(*sorted_data))

def plot_metrics(dataset_name, file_suffix):
    dataset_models = [model for model in models if model["dataset"] == dataset_name]
    
    if not dataset_models:
        print(f"No models found for {dataset_name}.")
        return

    methods = [model["method"] for model in dataset_models]
    mse_means = [model["results"]["MSE - mean"] for model in dataset_models]
    mse_stds = [model["results"]["MSE - std"] for model in dataset_models]
    r2_means = [model["results"]["R2 - mean"] for model in dataset_models]
    r2_stds = [model["results"]["R2 - std"] for model in dataset_models]
    train_times = [model["train_time"] for model in dataset_models]
    inference_times = [model["inference_time"] for model in dataset_models]

    # Sort methods and corresponding metrics
    sorted_data = sort_methods([mse_means, mse_stds, r2_means, r2_stds, train_times, inference_times], methods, method_order)
    methods, mse_means, mse_stds, r2_means, r2_stds, train_times, inference_times = sorted_data

    # MSE Plot
    plt.figure(figsize=(12, 6))
    plt.bar(methods, mse_means, yerr=mse_stds, capsize=5)
    plt.title(f'Mean Squared Error (MSE) - {dataset_name}')
    plt.ylabel('MSE')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'output/mse_plot_{file_suffix}.png')
    plt.show()

    # R2 Score Plot
    plt.figure(figsize=(12, 6))
    plt.bar(methods, r2_means, yerr=r2_stds, capsize=5)
    plt.title(f'R2 Score - {dataset_name}')
    plt.ylabel('R2 Score')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'output/r2_score_plot_{file_suffix}.png')
    plt.show()

    # Training and Inference Time Plot
    plt.figure(figsize=(12, 6))
    index = np.arange(len(methods))
    plt.bar(index, train_times, bar_width, label='Train Time')
    plt.bar(index + bar_width, inference_times, bar_width, label='Inference Time')
    plt.title(f'Training and Inference Time - {dataset_name}')
    plt.ylabel('Time (seconds)')
    plt.xticks(index + bar_width / 2, methods, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'output/training_inference_time_plot_{file_suffix}.png')
    plt.show()

# Iterate through the datasets and generate plots
for dataset in datasets:
    plot_metrics(dataset["name"], dataset["file_suffix"])
