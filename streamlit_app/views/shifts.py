import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000/api/v1"

def show_shifts():

    st.title("Shift Management")

    try:

        response = requests.get(
            f"{API}/shifts"
        )

        data = response.json()

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            width='stretch'
        )

    except Exception as e:

        st.error(str(e))