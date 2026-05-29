import streamlit as st
import requests

API = "http://127.0.0.1:8000/api/v1"


def show_notifications():

    st.title("My Notifications")

    emp_id = st.session_state.emp_id

    try:

        response = requests.get(
            f"{API}/notifications/{emp_id}"
        )

        if response.status_code != 200:

            st.error(
                "Failed to load notifications"
            )

            return

        notifications = response.json()

        if not notifications:

            st.info(
                "No notifications available"
            )

            return

        for item in notifications:

            with st.container():

                st.subheader(
                    item["title"]
                )

                st.write(
                    item["message"]
                )

                st.caption(
                    item["created_at"]
                )

                st.divider()

    except Exception as e:

        st.error(str(e))

