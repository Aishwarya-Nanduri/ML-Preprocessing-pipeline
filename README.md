# 📊 ML Data Preprocessing Pipeline

A modular Machine Learning data preprocessing pipeline built using **Python, Pandas, and NumPy**.  

This project demonstrates how raw data is cleaned, transformed, encoded, and scaled before being used for model training.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Preprocessing Workflow](#-preprocessing-workflow)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Output](#-output)
- [Learning Outcomes](#-learning-outcomes)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

## 🚀 Project Overview

Data preprocessing is a critical step in the Machine Learning lifecycle.  
Poor data quality leads to poor model performance.

This project implements a clean and reusable preprocessing pipeline that:

- Loads raw data
- Handles missing values
- Encodes categorical features
- Scales numerical features
- Saves the processed dataset

---

## ✅ Features

- 📥 Modular data loading
- 🧹 Missing value handling (Mean imputation)
- 🔤 Label Encoding for binary categorical variables
- 🧩 One-Hot Encoding for multi-class categorical variables
- 📊 Min-Max Normalization
- 📈 Standardization (Z-score scaling)
- 💾 Processed dataset export
- 🗂 Clean and scalable project structure

---

## 🛠 Tech Stack

- **Python 3.x**
- **Pandas**
- **NumPy**
- **Git & GitHub**

---

## 📂 Project Structure

```
ML-Preprocessing-pipeline/
│
├── data/
│   └── students.csv              # Raw dataset
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py            # Loads dataset
│   └── preprocessing.py          # Cleaning & transformation logic
│
├── outputs/
│   └── processed_students.csv    # Cleaned dataset (generated)
│
├── main.py                       # Entry point
├── requirements.txt              # Dependencies
└── README.md
```

---

## 🔄 Preprocessing Workflow

### 1️⃣ Data Loading
- Reads CSV file using a modular data loader.
- Separates data access logic from processing logic.

### 2️⃣ Handling Missing Values
- Converts numeric columns safely using `pd.to_numeric()`
- Replaces missing values using mean imputation
- Prevents ML model errors caused by NaN values

### 3️⃣ Encoding Categorical Variables
- **Label Encoding** for binary variable (Gender)
- **One-Hot Encoding** for multi-category variable (City)
- Ensures model compatibility with numerical input

### 4️⃣ Feature Scaling
- **Min-Max Normalization** applied to Marks (range: 0–1)
- **Standardization** applied to Age (mean = 0, std = 1)
- Improves model stability and convergence

### 5️⃣ Export Processed Data
- Saves clean dataset into `outputs/` folder
- Makes data reusable for model training

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/Aishwarya-Nanduri/ML-Preprocessing-pipeline.git
cd ML-Preprocessing-pipeline
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the preprocessing pipeline:

```
python main.py
```

The processed dataset will be automatically generated.

---

## 📤 Output

After execution:

```
outputs/processed_students.csv
```

The dataset will:
- Contain no missing values
- Have encoded categorical variables
- Have scaled numerical features

---

## 🎓 Learning Outcomes

Through this project:

- Understood importance of data preprocessing
- Applied imputation techniques
- Implemented encoding strategies
- Performed feature scaling
- Practiced modular code organization
- Used Git for version control

---

## 🔮 Future Enhancements

- Add train-test split
- Integrate Scikit-learn Pipeline
- Add model training
- Add logging system
- Deploy as a web app

---

## 👩‍💻 Author

**Aishwarya Nanduri**  
CSE (AI & ML) Student  
Interested in Machine Learning, Data Science, and AI Development  

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub.
