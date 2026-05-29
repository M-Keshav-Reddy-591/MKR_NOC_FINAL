import streamlit as st
import requests
import pandas as pd
from datetime import date

API = "http://127.0.0.1:8000"


def show_employee_attendance():

    st.title("My Attendance")

    emp_id = st.session_state.emp_id

    today = str(date.today())

    # =====================================================
    # GET TODAY SHIFTS
    # =====================================================

    shift_response = requests.get(
        f"{API}/api/v1/shifts/{emp_id}/{today}"
    )

    shifts = []

    if shift_response.status_code == 200:

        shifts = shift_response.json()

    st.subheader("Mark Attendance")

    if shifts:

        shift_options = [
            shift["shift_name"]
            for shift in shifts
        ]

        selected_shift = st.selectbox(
            "Select Shift",
            shift_options
        )

        status = st.selectbox(
            "Status",
            [
                "Present",
                "Absent",
                "Leave"
            ]
        )
        check_response = requests.get(
            f"{API}/api/v1/attendance/employee/{emp_id}"
        )

        already_marked = False

        if check_response.status_code == 200:

            records = check_response.json()

            for row in records:

                if (

                    row["date"] == today

                    and

                    row["shift_name"] == selected_shift

                ):

                    already_marked = True

        if already_marked:

            st.success(
                "Attendance already marked"
            )

        else:

            if st.button(
            "Mark Attendance",
            width="stretch"
                ):

                    response = requests.post(

                        f"{API}/api/v1/attendance/manual",

                        json={

                            "employee_id": emp_id,

                            "attendance_date": today,

                            "shift_name": selected_shift,

                            "status": status

                        }
                    )

                    if response.status_code == 200:

                        st.success(
                            "Attendance marked successfully"
                        )

                    else:

                        st.error(
                            "Unable to mark attendance"
                        )

    else:

        st.warning(
            "No shifts assigned for today"
        )

    st.divider()

    # =====================================================
    # ATTENDANCE HISTORY
    # =====================================================

    response = requests.get(
        f"{API}/api/v1/attendance/employee/{emp_id}"
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