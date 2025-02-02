import pandas as pd
import numpy as np
import sys
import os
import matplotlib.pyplot as plt

def load_data(file_path):
    """Loads dataset from CSV or XLSX file."""
    if not os.path.isfile(file_path):
        print("Error: File not found.")
        sys.exit(1)

    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        print("Error: Unsupported file format. Please use CSV or XLSX.")
        sys.exit(1)

def normalize_matrix(decision_matrix):
    """Normalize the decision matrix using vector normalization."""
    return decision_matrix / np.sqrt(np.sum(decision_matrix ** 2, axis=0))

def apply_topsis(data, weights, impacts):
    """Applies the TOPSIS algorithm to rank text generation models."""
    decision_matrix = data.iloc[:, 1:].values
    num_criteria = decision_matrix.shape[1]

    if len(weights) != num_criteria or len(impacts) != num_criteria:
        print("Error: Number of weights and impacts must match the number of criteria.")
        sys.exit(1)

    # Normalize and apply weights
    normalized_matrix = normalize_matrix(decision_matrix)
    weighted_matrix = normalized_matrix * weights

    # Determine ideal best and worst solutions
    ideal_best = [np.max(weighted_matrix[:, i]) if impacts[i] == '+' else np.min(weighted_matrix[:, i]) for i in range(num_criteria)]
    ideal_worst = [np.min(weighted_matrix[:, i]) if impacts[i] == '+' else np.max(weighted_matrix[:, i]) for i in range(num_criteria)]

    # Compute distances to ideal best and worst
    distance_to_best = np.sqrt(np.sum((weighted_matrix - ideal_best) ** 2, axis=1))
    distance_to_worst = np.sqrt(np.sum((weighted_matrix - ideal_worst) ** 2, axis=1))

    # Compute TOPSIS scores
    scores = distance_to_worst / (distance_to_best + distance_to_worst)
    
    # Append scores and rank to dataframe
    data['Topsis Score'] = scores
    data['Rank'] = scores.argsort()[::-1] + 1
    return data

def visualize_results(data):
    """Generates bar chart for TOPSIS ranking."""
    plt.figure(figsize=(10, 6))
    plt.barh(data['Model Name'], data['Topsis Score'], color='skyblue')
    plt.xlabel("Topsis Score")
    plt.ylabel("Models")
    plt.title("TOPSIS Ranking of Text Generation Models")
    plt.gca().invert_yaxis()
    plt.show()

def main():
    """Main function to run TOPSIS for text generation models."""
    if len(sys.argv) != 5:
        print("Usage: python <script_name.py> <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(',')))
    impacts = sys.argv[3].split(',')
    output_file = sys.argv[4]

    data = load_data(input_file)
    result = apply_topsis(data, weights, impacts)
    
    # Save output
    if output_file.endswith('.csv'):
        result.to_csv(output_file, index=False)
    elif output_file.endswith('.xlsx'):
        result.to_excel(output_file, index=False)
    else:
        print("Error: Unsupported output file format. Please use CSV or XLSX.")
        sys.exit(1)

    print(f"Results successfully saved to {output_file}")
    visualize_results(result)

if __name__ == "__main__":
    main()
