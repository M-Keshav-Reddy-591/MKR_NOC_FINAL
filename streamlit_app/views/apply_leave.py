import streamlit as st
import requests
import pandas as pd
from datetime import date


API_URL = "http://127.0.0.1:8000"


def show_apply_leave():

    st.title("Apply Leave")

    emp_id = st.session_state.emp_id

    leave_date = st.date_input(
        "Leave Date"
    )

    # =====================================================
    # FETCH SHIFTS
    # =====================================================

    shift_response = requests.get(

        f"{API_URL}/api/v1/shifts/{emp_id}/{leave_date}"

    )

    shifts = []

    if shift_response.status_code == 200:

        shifts = shift_response.json()

    shift_names = []

    for shift in shifts:

        if isinstance(shift, dict):

            shift_names.append(
                shift["shift_name"]
            )

        else:

            shift_names.append(shift)

    if not shift_names:

        st.warning(
            "No shifts assigned for this date"
        )

        return

    selected_shift = st.selectbox(
        "Select Shift",
        shift_names
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

    # =====================================================
    # APPLY LEAVE
    # =====================================================

    if st.button(
        "Apply Leave",
        key="apply_leave_btn"
    ):

        payload = {

            "employee_id": emp_id,

            "leave_date": str(
                leave_date
            ),

            "shift_name": selected_shift,

            "leave_type": leave_type,

            "reason": reason

        }

        response = requests.post(

            f"{API_URL}/api/v1/leaves/apply",

            json=payload

        )

        # ============================================
        # SUCCESS
        # ============================================

        if response.status_code == 200:

            st.success(
                "Leave applied successfully"
            )

        # ============================================
        # HANDLE ERRORS
        # ============================================

        else:

            try:

                error_message = response.json().get(
                    "detail",
                    "Unknown Error"
                )

                st.error(error_message)

            except:

                st.error(
                    f"Server Error: {response.text}"
                )

    st.divider()

    # =====================================================
    # MY LEAVES
    # =====================================================

    st.subheader(
        "My Leave Requests"
    )

    response = requests.get(

        f"{API_URL}/api/v1/leaves/employee/{emp_id}"

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
                "No leave requests found"
            )