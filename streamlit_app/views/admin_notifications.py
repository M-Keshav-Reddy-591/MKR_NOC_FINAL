import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000/api/v1"


def show_admin_notifications():

    st.title("Admin Notifications")

    try:

        response = requests.get(
            f"{API}/notifications/admin/all"
        )

        if response.status_code != 200:

            st.error(
                "Failed to load notifications"
            )

            return

        data = response.json()

        if not data:

            st.info(
                "No notifications found"
            )

            return

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            width="stretch"
        )

    except Exception as e:

        st.error(str(e))