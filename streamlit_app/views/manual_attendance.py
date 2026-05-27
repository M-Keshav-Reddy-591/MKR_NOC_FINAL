import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"


def show_manual_attendance():

    st.title("Manual Attendance")

    employee_id = st.text_input(
        "Employee ID"
    )

    status = st.selectbox(
        "Status",
        ["Present", "Absent", "Leave"]
    )

    if st.button(
        "Mark Attendance",
        width="stretch"
    ):

        response = requests.post(

            f"{API}/api/v1/attendance/manual",

            json={
                "employee_id": employee_id,
                "status": status
            }
        )

        st.success(
            response.json()["message"]
        )

    st.divider()

    attendance = requests.get(
        f"{API}/api/v1/attendance/"
    )

    if attendance.status_code == 200:

        data = attendance.json()

        if data:

            df = pd.DataFrame(data)

            st.dataframe(
                df,
                width="stretch"
            )