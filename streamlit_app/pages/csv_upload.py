import streamlit as st
import pandas as pd

st.title("CSV ROSTER UPLOAD")

file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if file:

    df = pd.read_csv(file)

    st.dataframe(df)

    st.success(
        "CSV Loaded Successfully"
    )