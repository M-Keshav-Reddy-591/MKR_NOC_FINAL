import streamlit as st
import pandas as pd


def show_csv_upload():

    st.title("CSV UPLOAD")

    file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if file:

        df = pd.read_csv(file)

        st.dataframe(
            df,
            width='stretch'
        )