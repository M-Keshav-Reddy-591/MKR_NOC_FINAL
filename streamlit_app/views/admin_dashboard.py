import streamlit as st
import requests

API = "http://127.0.0.1:8000/api/v1"

def show_admin_dashboard():

    st.title("Admin Dashboard")

    try:

        response = requests.get(
            f"{API}/dashboard/stats"
        )

        data = response.json()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Employees",
            data.get("total_employees", 0)
        )

        col2.metric(
            "Present",
            data.get("present_today", 0)
        )

        col3.metric(
            "Absent",
            data.get("absent_today", 0)
        )

        col4.metric(
            "Shifts",
            data.get("total_shifts", 0)
        )

        st.success("System Running Successfully")

    except Exception as e:

        st.error(str(e))