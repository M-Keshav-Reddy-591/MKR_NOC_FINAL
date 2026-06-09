import streamlit as st
import requests
import pandas as pd

# API_URL = "http://192.168.100.237:8000"
API_URL = "http://172.16.100.150:8000"


def show_browser_sessions():

    st.title("Browser Sessions")

    try:

        response = requests.get(
            f"{API_URL}/api/v1/sessions/"
        )

        if response.status_code == 200:

            data = response.json()

            if len(data) > 0:

                df = pd.DataFrame(data)

                st.dataframe(
                    df,
                    width="stretch"
                )

            else:

                st.info(
                    "No sessions found"
                )

        else:

            st.error(
                response.text
            )

    except Exception as e:

        st.error(
            str(e)
        )