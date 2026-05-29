import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"


def show_admin_dashboard():

    st.title("Admin Dashboard")

    # =====================================================
    # DASHBOARD STATS
    # =====================================================

    stats_response = requests.get(
        f"{API}/api/v1/dashboard/stats"
    )

    if stats_response.status_code == 200:

        stats = stats_response.json()

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Employees",
                stats["employees"]
            )

        with col2:

            st.metric(
                "Present",
                stats["present"]
            )

        with col3:

            st.metric(
                "Absent",
                stats["absent"]
            )

    st.divider()

    # # =====================================================
    # # PASSWORD CHANGE LOGS
    # # =====================================================

    # st.subheader("Password Change Logs")

    # logs_response = requests.get(
    #     f"{API}/api/v1/auth/password-logs"
    # )

    # if logs_response.status_code == 200:

    #     logs = logs_response.json()

    #     if logs:

    #         df = pd.DataFrame(logs)

    #         st.dataframe(
    #             df,
    #             width="stretch"
    #         )

    #     else:

    #         st.info(
    #             "No password change logs"
    #         )

    # else:

    #     st.error(
    #         "Failed to load password logs"
    #     )