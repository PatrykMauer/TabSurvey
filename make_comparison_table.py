import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load model results from JSON file
with open('output/all_results.json') as f:
    models = json.load(f)

r2_data = []
for entry in models:
    method = entry["method"]
    dataset = entry["dataset"]
    r2_mean = entry["results"]["R2 - mean"]
    r2_std = entry["results"]["R2 - std"]
    r2_value = f"{r2_mean:.3f} ± {r2_std:.3f}"
    r2_data.append([method, dataset, r2_value])

# Create DataFrame
df_r2 = pd.DataFrame(r2_data, columns=["Method", "Dataset", "R2 Mean ± Std"])

# Group by Method and Dataset to handle duplicates
df_r2_grouped = df_r2.groupby(["Method", "Dataset"]).agg(lambda x: ' / '.join(x)).reset_index()

# Pivot the DataFrame
pivot_table = df_r2_grouped.pivot(index='Method', columns='Dataset', values='R2 Mean ± Std')

# Save the pivot table to a CSV file
output_file_pivot = "output/r2_pivot_table_3.csv"
pivot_table.to_csv(output_file_pivot)