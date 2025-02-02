import pandas as pd

def generate_textgen_csv():
    data = {
        "Model Name": ["GPT-3", "GPT-2", "T5", "BART", "XLNet"],
        "BLEU Score": [85.3, 72.4, 81.2, 78.9, 74.5],
        "ROUGE Score": [88.1, 75.6, 83.5, 80.2, 77.0],
        "METEOR Score": [78.2, 65.4, 74.5, 72.8, 68.3],
        "Diversity Score": [0.85, 0.78, 0.82, 0.80, 0.77],
        "Coherence Score": [4.5, 3.9, 4.3, 4.1, 3.8]
    }
    
    df = pd.DataFrame(data)
    file_name = "text_generation_models.csv"
    df.to_csv(file_name, index=False)
    print(f"CSV file '{file_name}' generated successfully!")

if __name__ == "__main__":
    generate_textgen_csv()
