# AutoJudge – Programming Problem Difficulty Prediction

AutoJudge is a machine-learning project that **estimates the difficulty of programming problems using only their text**.  
The system supports two main prediction tasks:

1. **Difficulty Class** — Easy / Medium / Hard  
2. **Difficulty Score** — A continuous numerical difficulty estimate  

A lightweight Streamlit web interface is included for real-time predictions.

---

## 📌 Project Summary  

Competitive programming platforms often assign difficulty labels manually, which can be subjective, inconsistent, and slow.  
AutoJudge aims to automate this process by analyzing the problem statement and predicting its difficulty level without using submission trends or platform metadata.

The solution relies **solely on textual content**, following the project constraint of no external information.

---

## 📊 Dataset  

The dataset consists of real programming challenges collected from online competitive programming platforms.  
Each sample contains:

- `title`  
- `description`  
- `input_description`  
- `output_description`  
- `problem_class` (Easy / Medium / Hard)  
- `problem_score` (numerical difficulty)

The original dataset was provided in JSONL format and converted to CSV for preprocessing.

---

## 🛠 Preprocessing Workflow  

The data preparation stage included:

- Filling missing text fields with empty strings  
- Concatenating all textual fields into a single unified feature  
- Applying **log transform** to difficulty scores to reduce skew  
- Extracting additional numerical indicators directly from text  

Final training text was structured as:


---

## 🔍 Feature Engineering  

Text was converted into numerical form using a **hybrid feature approach**.

### ✔ TF-IDF Features  
- Unigrams, bigrams, and trigrams  
- Stopword removal  
- Sublinear term frequency scaling  
- Feature count limited for efficiency  

### ✔ Handcrafted Text Features  
Extracted directly from raw text:

- Total character length of the problem statement  
- Count of mathematical symbols (`=`, `<`, `*`, `/`, `^`, etc.)  
- Keyword frequency features for:
  `dp`, `graph`, `tree`, `recursion`, `greedy`, `modulo`

All features strictly originate from text, ensuring full adherence to project rules.

---

## 🤖 Models  

Two independent models were trained:

### 🔹 Difficulty Classification — Random forest classifier
- Predicts Easy / Medium / Hard  

### 🔹 Difficulty Regression — XGBoost  
- Predicts numeric difficulty score  
- Trained on log-transformed labels  
- Captures non-linear feature relationships effectively

Both models are stored using `joblib` for easy reuse.

---

## 📈 Evaluation  

### Classification Performance  
- **Test Accuracy:** ~57.7%  
- **Cross-Validation Mean Accuracy:** ~52.5%  
- Confusion matrix shows Medium is best recognized, with expected overlap between Medium and Hard.

### Regression Performance  
(Results reported on log-transformed target)
- **MAE:** ~0.294  
- **RMSE:** ~0.357  

These values show reasonable predictive power given that difficulty labels are inherently subjective.

---

## 🌐 Web Application  

A user-friendly Streamlit interface enables live testing.

Users can enter:
- Problem description  
- Input specification  
- Output specification  

The app returns:
- Predicted difficulty class  
- Predicted difficulty score  

Runs locally.

---
👤 Author
Name: Mohit Sharma
Enrollment no: 23112062
