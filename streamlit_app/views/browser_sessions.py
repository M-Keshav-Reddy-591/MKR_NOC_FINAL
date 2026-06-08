import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"


def show_browser_sessions():

    st.title(
        "Browser Sessions"
    )

    response = requests.get(
        f"{API_URL}/api/v1/sessions/"
    )

    if response.status_code == 200:

        data = response.json()

        if data:

            df = pd.DataFrame(data)

            st.dataframe(
                df,
                width="stretch"
            )

        else:

            st.info(
                "No sessions found"
            )