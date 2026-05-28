import streamlit as st
import requests
import pandas as pd
from datetime import date

API = "http://127.0.0.1:8000"


def show_manual_attendance():

    st.title("Manual Attendance")

    employee_id = st.text_input(
        "Employee ID"
    )

    attendance_date = st.date_input(
        "Attendance Date",
        value=date.today()
    )

    shifts = []

    if employee_id:

        response = requests.get(

            f"{API}/api/v1/shifts/{employee_id}/{attendance_date}"

        )

        if response.status_code == 200:

            shifts = response.json()

    if not shifts:

        st.warning(
            "No shifts assigned for this employee on selected date"
        )

        shift_name = ""

    else:

        shift_name = st.selectbox(
            "Assigned Shift",
            shifts
        )

    status = st.selectbox(
        "Status",
        [
            "Present",
            "Absent",
            "Leave"
        ]
    )

    if st.button(
        "Mark Attendance",
        width="stretch"
    ):

        response = requests.post(

            f"{API}/api/v1/attendance/manual",

            json={

                "employee_id": employee_id,

                "attendance_date": str(
                    attendance_date
                ),

                "shift_name": shift_name,

                "status": status

            }
        )

        if response.status_code == 200:

            st.success(
                response.json()["message"]
            )

        else:

            st.error(
                response.text
            )

    st.divider()

    response = requests.get(
        f"{API}/api/v1/attendance/"
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

            st.warning(
                "No attendance records found"
            )