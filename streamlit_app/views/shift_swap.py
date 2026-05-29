import streamlit as st
import requests
from datetime import date

API = "http://127.0.0.1:8000"


def show_shift_swap():

    st.title("Shift Swap")

    response = requests.get(
        f"{API}/api/v1/employees"
    )

    if response.status_code != 200:

        st.error(
            "Failed to load employees"
        )

        return

    employees = response.json()

    employee_options = []

    for emp in employees:

        if emp["emp_id"] != st.session_state.emp_id:

            employee_options.append(
                f"{emp['emp_name']} ({emp['emp_id']})"
            )

    selected = st.selectbox(
        "Select Employee",
        employee_options
    )

    target_emp_id = selected.split("(")[1].replace(")", "")

    shift_date = st.date_input(
        "Shift Date",
        value=date.today()
    )

    if st.button(
        "Request Shift Swap",
        width="stretch"
    ):

        response = requests.post(

            f"{API}/api/v1/swaps/request",

            json={

                "requester_id":
                st.session_state.emp_id,

                "target_employee_id":
                target_emp_id,

                "shift_date":
                str(shift_date)

            }

        )

        data = response.json()

        if response.status_code == 200:

            st.success(
                data["message"]
            )

        else:

            st.error(
                data["detail"]
            )


    st.divider()

    # =====================================================
    # SWAP HISTORY
    # =====================================================

    st.subheader("Swap Request History")

    try:

        history_response = requests.get(
            f"{API}/swap/my-requests/{emp_id}"
        )

        if history_response.status_code == 200:

            history = history_response.json()

            if history:

                for item in history:

                    status = item["status"]

                    if status == "Approved":

                        st.success(

                            f"""
Request To: {item['target_employee']}

Date: {item['date']}

Your Shift: {item['your_shift']}

Requested Shift: {item['target_shift']}

Status: {status}
"""
                        )

                    elif status == "Rejected":

                        st.error(

                            f"""
Request To: {item['target_employee']}

Date: {item['date']}

Your Shift: {item['your_shift']}

Requested Shift: {item['target_shift']}

Status: {status}
"""
                        )

                    else:

                        st.warning(

                            f"""
Request To: {item['target_employee']}

Date: {item['date']}

Your Shift: {item['your_shift']}

Requested Shift: {item['target_shift']}

Status: {status}
"""
                        )

            else:

                st.info(
                    "No swap requests"
                )

    except Exception as e:

        st.error(str(e))

