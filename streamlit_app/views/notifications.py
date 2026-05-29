
import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"


def show_notifications():

    st.title("Notifications")

    role = st.session_state.role

    if role.lower() == "admin":

        response = requests.get(
            f"{API}/api/v1/notifications/admin/all"
        )

    else:

        emp_id = st.session_state.emp_id

        response = requests.get(
            f"{API}/api/v1/notifications/{emp_id}"
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
                "No notifications"
            )

    else:

        st.error(
            "Failed to load notifications"
        )

