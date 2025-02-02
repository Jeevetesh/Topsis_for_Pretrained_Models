# TOPSIS for Text Generation Models

## 📌 Project Overview
This project implements the **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** method to rank pre-trained text generation models based on multiple performance metrics.

## 📂 Folder Structure
- **Generate Textgen Csv** → Python script to generate the dataset (`text_generation_models.xlsx`).
- **output.xlsx** → The final ranked models with their TOPSIS scores.
- **output.png** → Graphical visualization of the model rankings.
- **text_generation_models.xlsx** → The dataset containing model performance metrics.
- **topsis.py** → Python script that applies the TOPSIS algorithm to rank the models.

## 🛠️ Requirements
Before running the script, install the required dependencies:

```bash
pip install pandas numpy matplotlib openpyxl
```

## 🚀 How to Use
### **Step 1: Generate the Dataset**
Run the dataset generation script to create the `text_generation_models.xlsx` file:
```bash
python Generate_Textgen_Csv.py
```

### **Step 2: Apply TOPSIS**
Execute the TOPSIS script to rank the models:
```bash
python topsis.py text_generation_models.xlsx "1,1,1,1,1" "+,+,+,+,+" output.xlsx
```

### **Step 3: View the Results**
- The **output.xlsx** file will contain the ranked models.
- The **output.png** will show a graphical representation of the rankings.

## 📜 Example Output Table
| Model Name | TOPSIS Score | Rank |
|------------|-------------|------|
| GPT-3      | 0.89        | 1    |
| T5         | 0.81        | 2    |
| BART       | 0.79        | 3    |
| XLNet      | 0.72        | 4    |
| GPT-2      | 0.68        | 5    |

## 📈 Visualization
The ranking is represented in `output.png`, showing the comparative performance of models.

## 📝 Conclusion
This project applies **TOPSIS** to rank **text generation models** based on multiple evaluation metrics. The ranking provides insights into which model performs the best across various dimensions.

📩 Feel free to reach out if you have any questions or need modifications! 🚀

