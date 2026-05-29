import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"


def show_password_logs():

    st.title("Password Change Logs")

    try:

        response = requests.get(
            f"{API}/api/v1/auth/password-logs"
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
                    "No password logs found"
                )

        else:

            st.error(
                "Failed to load password logs"
            )

    except Exception as e:

        st.error(str(e))