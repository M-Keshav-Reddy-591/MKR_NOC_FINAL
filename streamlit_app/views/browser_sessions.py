import streamlit as st
import requests
import pandas as pd

API_URL = "http://192.168.100.237:8000"


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
                    use_container_width=True
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