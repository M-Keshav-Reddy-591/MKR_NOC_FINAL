import streamlit as st
import pandas as pd
import requests

API = "http://127.0.0.1:8000/api/v1"

def show_csv_upload():

    st.title("CSV Shift Upload")

    file = st.file_uploader(
        "Upload Shift CSV",
        type=["csv"]
    )

    if file:

        df = pd.read_csv(file)

        st.dataframe(
            df,
            width="stretch"
        )

        if st.button("Upload To Database"):

            records = df.to_dict(
                orient="records"
            )

            try:

                response = requests.post(

                    f"{API}/shifts/upload-csv",

                    json=records
                )

                if response.status_code == 200:

                    st.success(
                        "CSV Uploaded Successfully"
                    )

                else:

                    st.error(
                        response.text
                    )

            except Exception as e:

                st.error(str(e))