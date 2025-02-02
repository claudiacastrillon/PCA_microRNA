# 🧬 PCA Analysis on MicroRNA Data

## 📌 Overview
This repository contains Python code for performing **Principal Component Analysis (PCA)** on microRNA data to reduce dimensionality before a **permutation analysis**. The goal is to identify the **top 13 contributing microRNAs** and analyze their impact on principal components.

## 🔬 Methodology
- PCA is a statistical technique that uses **orthogonal transformation** to convert possibly correlated variables into a set of **linearly uncorrelated principal components**.
- The **contribution scores** were calculated as the sum of the absolute values of the loadings of each microRNA.
- Data was generated using a **log-normal distribution** with some correlation between features to mimic real biological datasets.
- The explained variance by each principal component is visualized in a **bar plot**.
- The **reduced dataset** is saved in an **Excel file** using the `openpyxl` library.

## 📦 Dependencies
Ensure you have the following Python libraries installed:

```bash
pip install pandas numpy scikit-learn matplotlib openpyxl
```

## 🛠️ Usage
1️⃣ **Clone this repository:**
```bash
git clone https://github.com/claudiacastrillon/PCA_microRNA.git
```

2️⃣ **Navigate to the project folder:**
```bash
cd PCA_microRNA
```

3️⃣ **Run the PCA analysis script:**
```bash
python PCA.py
```


## 📊 Output

Bar plot showing explained variance for each principal component.

Excel file containing the reduced microRNA expression dataset.

## 🤝 Contributions

Feel free to contribute by submitting pull requests or reporting issues!

## 📜 License

This project is open-source. See LICENSE for details.

📩 Contact

For inquiries, contact claudiacastrillon via GitHub. 
