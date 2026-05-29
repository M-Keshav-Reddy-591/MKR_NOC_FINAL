import streamlit as st
import requests
import pandas as pd
from datetime import date


API_URL = "http://127.0.0.1:8000"


def show_manual_attendance():

    st.title("Manual Attendance")

    # =====================================================
    # EMPLOYEE
    # =====================================================

    employee_id = st.text_input(
        "Employee ID"
    )

    attendance_date = st.date_input(
        "Attendance Date",
        value=date.today()
    )

    shifts = []

    # =====================================================
    # FETCH SHIFTS
    # =====================================================

    if employee_id:

        response = requests.get(

            f"{API_URL}/api/v1/shifts/{employee_id}/{attendance_date}"

        )

        if response.status_code == 200:

            shifts = response.json()

    shift_names = []

    for shift in shifts:

        if isinstance(shift, dict):

            shift_names.append(
                shift["shift_name"]
            )

        else:

            shift_names.append(
                shift
            )

    # =====================================================
    # SHIFT SELECT
    # =====================================================

    if shift_names:

        selected_shift = st.selectbox(
            "Assigned Shift",
            shift_names
        )

    else:

        selected_shift = st.text_input(
            "Shift Name"
        )

    # =====================================================
    # STATUS
    # =====================================================

    status = st.selectbox(

        "Attendance Status",

        [
            "Present",
            "Absent",
            "Leave"
        ]

    )

    # =====================================================
    # MARK ATTENDANCE
    # =====================================================

    if st.button(
        "Mark Attendance",
        width="stretch"
    ):

        payload = {

            "employee_id": employee_id,

            "attendance_date": str(
                attendance_date
            ),

            "shift_name": selected_shift,

            "status": status

        }

        response = requests.post(

            f"{API_URL}/api/v1/attendance/manual",

            json=payload

        )

        if response.status_code == 200:

            st.success(
                "Attendance marked successfully"
            )

        else:

            try:

                st.error(
                    response.json()["detail"]
                )

            except:

                st.error(
                    response.text
                )

    st.divider()

    # =====================================================
    # ATTENDANCE LIST
    # =====================================================

    st.subheader(
        "Attendance Records"
    )

    response = requests.get(
        f"{API_URL}/api/v1/attendance/"
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
                "No attendance records found"
            )