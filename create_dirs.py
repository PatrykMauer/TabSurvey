import os
import yaml

# Define the paths
config_dir = 'config'
output_dir = 'output/CatBoost'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to process YAML files
def process_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        if 'dataset' in data:
            dataset_name = data['dataset']
            dataset_dir = os.path.join(output_dir, dataset_name)
            os.makedirs(dataset_dir, exist_ok=True)
            print(f"Created directory: {dataset_dir}")

# Iterate over YAML files in the config directory
for filename in os.listdir(config_dir):
    if filename.endswith('.yml') or filename.endswith('.yaml'):
        file_path = os.path.join(config_dir, filename)
        process_yaml_file(file_path)
