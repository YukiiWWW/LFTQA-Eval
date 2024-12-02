import os, json
import pandas as pd
from scipy.stats import pearsonr
import numpy as np

def calculate_correlation(metric_filepath, human_filepath):
    data = pd.read_json(metric_filepath)
    human_comp_data = pd.read_json(human_filepath)

    merged_data = pd.merge(data, human_comp_data, on=['example_id', 'model'], suffixes=('_metric', '_human'))

    # Calculate instance-level Kendall Tau correlation for each example_id
    instance_tau_values = []
    for example_id in merged_data['example_id'].unique():
        example_data = merged_data[merged_data['example_id'] == example_id]

        tau, _ = pearsonr(example_data['score_metric'], example_data['score_human'])
        if not np.isnan(tau): 
            instance_tau_values.append(tau)

    instance_level_tau = np.mean(instance_tau_values)
    
    return instance_level_tau


results_dict = {}
for dataset in ["qtsumm", "fetaqa"]:
    for criteria in ["faithfulness", "comprehensiveness"]:
        metric_dir = f"scores/{dataset}/metric_scores"
        human_filepath = f"scores/{dataset}/human_scores/human_{criteria}_scores.json" 

        row_label = f"{dataset}-{criteria}"
        results_dict[row_label] = {}

        # Loop through all the metric files in the directory
        for metric_file in os.listdir(metric_dir):
            if metric_file.endswith('.json'):  # Avoid human comprehensiveness file itself
                metric_filepath = os.path.join(metric_dir, metric_file)
                metric_name = metric_file.replace('.json', '')  # Extract the metric name
                instance_tau = calculate_correlation(metric_filepath, human_filepath)
                # Store the instance-level tau in the dictionary
                results_dict[row_label][metric_name] = instance_tau

# Convert the results dictionary to a DataFrame for easy viewing
results_df = pd.DataFrame(results_dict)  # Transpose to get rows as dataset-criteria and columns as metrics

# Display the resulting table
# output to a csv file
results_df.round(3).to_csv("correlation_results.csv")
