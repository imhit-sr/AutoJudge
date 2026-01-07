import streamlit as st
import joblib
import numpy as np
import pandas as pd
import re


classifier = joblib.load("classifier.pkl")
regressor = joblib.load("regressor.pkl")


st.title("AutoJudge: Problem Difficulty Predictor")

description = st.text_area("Problem Description")
input_desc = st.text_area("Input Description")
output_desc = st.text_area("Output Description")

if st.button("Predict"):
    if description.strip() == "" or input_desc.strip() == "" or output_desc.strip() == "":
        st.warning("Please fill all fields.")
    else:

        full_text = description + " " + input_desc + " " + output_desc

        text_length = len(full_text)
        math_symbols = len(re.findall(r"[=<>+\-*/^]", full_text))

        keywords = ["dp", "graph", "tree", "recursion", "greedy", "modulo"]
        keyword_counts = {
            kw: len(re.findall(rf"\b{kw}\b", full_text.lower()))
            for kw in keywords
        }

        input_df = pd.DataFrame([{
            "text": full_text,
            "text_length": text_length,
            "math_symbols": math_symbols,
            **keyword_counts
        }])

        pred_class = classifier.predict(input_df)[0]
        pred_log_score = regressor.predict(input_df)[0]
        pred_score = np.expm1(pred_log_score)


        st.success(f"Predicted Difficulty Class: **{pred_class}**")
        st.success(f"Predicted Difficulty Score: **{round(pred_score, 2)}**")
