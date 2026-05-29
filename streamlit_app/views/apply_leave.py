import streamlit as st
import requests
import pandas as pd
from datetime import date

API = "http://127.0.0.1:8000"

def show_apply_leave():

    st.title("Apply Leave")

    leave_date = st.date_input(
        "Leave Date",
        value=date.today()
    )

    # FETCH SHIFTS

    shifts_response = requests.get(
        f"{API}/api/v1/shifts/{st.session_state.emp_id}/{leave_date}"
    )

    shift_options = []

    if shifts_response.status_code == 200:

        shift_options = shifts_response.json()

    if not shift_options:

        st.warning(
            "No shifts assigned on this date"
        )

        return

    shift_name = st.selectbox(
        "Select Shift",
        shift_options
    )

    leave_type = st.selectbox(
        "Leave Type",
        [
            "Sick Leave",
            "Casual Leave",
            "Emergency Leave"
        ]
    )

    reason = st.text_area(
        "Reason"
    )

    if st.button(
        "Apply Leave",
        width="stretch"
    ):

        response = requests.post(

            f"{API}/api/v1/leaves/apply",

            json={

                "employee_id": st.session_state.emp_id,

                "leave_date": str(leave_date),

                "shift_name": shift_name,

                "leave_type": leave_type,

                "reason": reason

            }
        )

        if response.status_code == 200:

            st.success(
                response.json()["message"]
            )

            st.rerun()

        else:

            st.error(
                response.json()["detail"]
            )

    st.divider()

    st.subheader("My Leave Requests")

    leave_response = requests.get(
        f"{API}/api/v1/leaves/employee/{st.session_state.emp_id}"
    )

    if leave_response.status_code == 200:

        data = leave_response.json()

        if data:

            df = pd.DataFrame(data)

            st.dataframe(
                df,
                width="stretch"
            )

        else:

            st.warning(
                "No leave requests found"
            )