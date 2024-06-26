# data.py

import streamlit as st
import pandas as pd



# Static dummy data (replace with your actual data loading code)
data = pd.read_csv("data/data_anonymized.csv")


# Data Exploration
st.header("Data")
st.write("To respect privacy, we have anonymized industry names, values, and other sensitive details in this project. However, the methodology and data proportions remain unchanged.") 
st.write("The data presented here has undergone thorough cleaning and engineering to ensure it is analysis-ready. It's important to clarify that this isn't the raw, original data collected. Instead, this version has been prepared specifically for demonstration purposes, showcasing our finalized approach and methodology.")

st.write("---")
st.subheader("Analized Dataframe:")

st.dataframe(data)






