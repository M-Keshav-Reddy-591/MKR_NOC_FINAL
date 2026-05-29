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

    shifts_response = requests.get(
        f"{API}/api/v1/shifts/{emp_id}/{today}"
    )

    shifts = []

    shift_details = {}

    if shifts_response.status_code == 200:

        shift_data = shifts_response.json()

        for row in shift_data:

            if isinstance(row, dict):

                shift_name = row.get(
                    "shift_name",
                    ""
                )

                shifts.append(
                    shift_name
                )

                shift_details[
                    shift_name
                ] = row

            else:

                shifts.append(row)

    # =====================================================
    # GET ATTENDANCE
    # =====================================================

    attendance_response = requests.get(
        f"{API}/api/v1/attendance/employee/{emp_id}"
    )

    attendance_data = []

    if attendance_response.status_code == 200:

        attendance_data = attendance_response.json()

    # =====================================================
    # MARK ATTENDANCE
    # =====================================================

    st.subheader("Mark Attendance")

    if shifts:

        selected_shift = st.selectbox(
            "Select Shift",
            shifts
        )

        # =================================================
        # SHOW SHIFT TIMINGS
        # =================================================

        shift_info = shift_details.get(
            selected_shift,
            {}
        )

        start_time = shift_info.get(
            "start_time",
            "-"
        )

        end_time = shift_info.get(
            "end_time",
            "-"
        )

        st.info(
            f"Shift Time : {start_time} → {end_time}"
        )

        # =================================================
        # CHECK DUPLICATE
        # =================================================

        already_marked = False

        for row in attendance_data:

            if (

                row["date"] == today

                and

                row["shift_name"] == selected_shift

            ):

                already_marked = True

                st.success(
                    f"Attendance already marked for {selected_shift}"
                )

                break

        # =================================================
        # MARK ATTENDANCE
        # =================================================

        if not already_marked:

            if st.button(
                "Mark Present",
                width="stretch"
            ):

                response = requests.post(

                    f"{API}/api/v1/attendance/mark",

                    json={

                        "employee_id": emp_id,

                        "attendance_date": today,

                        "shift_name": selected_shift

                    }

                )

                try:

                    data = response.json()

                    if response.status_code == 200:

                        st.success(
                            data["message"]
                        )

                        st.rerun()

                    else:

                        st.error(
                            data["detail"]
                        )

                except:

                    st.error(
                        "Backend error"
                    )

    else:

        st.warning(
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

        st.warning(
            "No attendance records"
        )

