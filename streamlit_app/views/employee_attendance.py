import streamlit as st
import requests
import pandas as pd
from datetime import date


API_URL = "http://127.0.0.1:8000"


def show_employee_attendance():

    st.title("My Attendance")

    emp_id = st.session_state.emp_id

    today = str(date.today())

    # =====================================================
    # FETCH TODAY SHIFTS
    # =====================================================

    shift_response = requests.get(

        f"{API_URL}/api/v1/shifts/{emp_id}/{today}"

    )

    shifts = []

    if shift_response.status_code == 200:

        shifts = shift_response.json()

    # =====================================================
    # FETCH ATTENDANCE
    # =====================================================

    attendance_response = requests.get(

        f"{API_URL}/api/v1/attendance/employee/{emp_id}"

    )

    attendance_data = []

    if attendance_response.status_code == 200:

        attendance_data = attendance_response.json()

    # =====================================================
    # MARK ATTENDANCE
    # =====================================================

    st.subheader("Today's Shifts")

    if shifts:

        for shift in shifts:

            shift_name = shift["shift_name"]

            already_marked = False

            for row in attendance_data:

                if (

                    row["date"] == today

                    and

                    row["shift"] == shift_name

                ):

                    already_marked = True
                    break

            st.write(
                f"Shift: {shift_name}"
            )

            if already_marked:

                st.success(
                    "Attendance Already Marked"
                )

            else:

                if st.button(
                    f"Mark Present - {shift_name}"
                ):

                    payload = {

                        "employee_id": emp_id,

                        "attendance_date": today,

                        "status": "Present",

                        "shift_name": shift_name

                    }

                    response = requests.post(

                        f"{API_URL}/api/v1/attendance/manual",

                        json=payload

                    )

                    if response.status_code == 200:

                        st.success(
                            "Attendance Marked"
                        )

                        st.rerun()

                    else:

                        try:

                            st.error(
                                response.json()["detail"]
                            )

                        except:

                            st.error(
                                "Server Error"
                            )

    else:

        st.info(
            "No shifts assigned today"
        )

    st.divider()

    # =====================================================
    # ATTENDANCE HISTORY
    # =====================================================

    st.subheader("Attendance History")

    if attendance_data:

        df = pd.DataFrame(
            attendance_data
        )

        st.dataframe(
            df,
            width="stretch"
        )

    else:

        st.info(
            "No attendance records found"
        )