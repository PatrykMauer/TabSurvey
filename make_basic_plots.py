import json
import matplotlib.pyplot as plt

# Load the JSON data from the file
file_path = "output/results_for_plotting.json"
with open(file_path, "r") as file:
    json_data = json.load(file)

# Initialize lists to store the data for plotting
methods = []
accuracies = []
train_times = []
inference_times = []

# Parse the JSON data
for entry in json_data:
    methods.append(entry["method"])
    accuracies.append(entry["results"]["Accuracy - mean"])
    train_times.append(entry["train_time"])
    inference_times.append(entry["inference_time"])

# Create the scatter plot for Training Time vs. Accuracy
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(train_times, accuracies, s=100, alpha=0.6, c='b')
for i, method in enumerate(methods):
    plt.text(train_times[i], accuracies[i], method, fontsize=9)
plt.xscale('log')
plt.xlabel('Training Time (seconds)')
plt.ylabel('Accuracy')
plt.title('Training Time vs Accuracy')

# Create the scatter plot for Inference Time vs. Accuracy
plt.subplot(1, 2, 2)
plt.scatter(inference_times, accuracies, s=100, alpha=0.6, c='r')
for i, method in enumerate(methods):
    plt.text(inference_times[i], accuracies[i], method, fontsize=9)
plt.xscale('log')
plt.xlabel('Inference Time (seconds)')
plt.ylabel('Accuracy')
plt.title('Inference Time vs Accuracy')

plt.tight_layout()

# Save the plots as images
train_time_plot_path = "output/training_time_vs_accuracy.png"
inference_time_plot_path = "output/inference_time_vs_accuracy.png"

plt.savefig(train_time_plot_path)
plt.savefig(inference_time_plot_path)
