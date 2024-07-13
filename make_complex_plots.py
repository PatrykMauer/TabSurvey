import json
import matplotlib.pyplot as plt
import os

# Load the JSON data from the file
file_path = "output/results_for_plotting.json"
with open(file_path, "r") as file:
    json_data = json.load(file)

# Initialize lists to store the data for plotting
methods = []
accuracies = []
auc_scores = []
log_losses = []
f1_scores = []
train_times = []
inference_times = []

# Parse the JSON data
for entry in json_data:
    methods.append(entry["method"])
    accuracies.append(entry["results"]["Accuracy - mean"])
    auc_scores.append(entry["results"]["AUC - mean"])
    log_losses.append(entry["results"]["Log Loss - mean"])
    f1_scores.append(entry["results"]["F1 score - mean"])
    train_times.append(entry["train_time"])
    inference_times.append(entry["inference_time"])

# Ensure the output directory exists
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to create and save scatter plots
def create_and_save_scatter_plot(x_data, y_data, x_label, y_label, title, filename):
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, s=100, alpha=0.6)
    for i, method in enumerate(methods):
        plt.text(x_data[i], y_data[i], method, fontsize=9)
    plt.xscale('log')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()

# Create and save all the required plots
create_and_save_scatter_plot(train_times, accuracies, 'Training Time (seconds)', 'Accuracy', 'Training Time vs Accuracy', 'training_time_vs_accuracy.png')
create_and_save_scatter_plot(inference_times, accuracies, 'Inference Time (seconds)', 'Accuracy', 'Inference Time vs Accuracy', 'inference_time_vs_accuracy.png')
create_and_save_scatter_plot(train_times, auc_scores, 'Training Time (seconds)', 'AUC', 'Training Time vs AUC', 'training_time_vs_auc.png')
create_and_save_scatter_plot(inference_times, auc_scores, 'Inference Time (seconds)', 'AUC', 'Inference Time vs AUC', 'inference_time_vs_auc.png')
create_and_save_scatter_plot(train_times, log_losses, 'Training Time (seconds)', 'Log Loss', 'Training Time vs Log Loss', 'training_time_vs_log_loss.png')
create_and_save_scatter_plot(inference_times, log_losses, 'Inference Time (seconds)', 'Log Loss', 'Inference Time vs Log Loss', 'inference_time_vs_log_loss.png')
create_and_save_scatter_plot(train_times, f1_scores, 'Training Time (seconds)', 'F1 Score', 'Training Time vs F1 Score', 'training_time_vs_f1_score.png')
create_and_save_scatter_plot(inference_times, f1_scores, 'Inference Time (seconds)', 'F1 Score', 'Inference Time vs F1 Score', 'inference_time_vs_f1_score.png')

print("Plots saved in the output directory.")
