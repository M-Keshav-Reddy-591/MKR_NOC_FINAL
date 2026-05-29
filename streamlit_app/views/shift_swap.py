import streamlit as st
import requests
from datetime import date

API = "http://127.0.0.1:8000"


def show_shift_swap():

    st.title("Shift Swap")

    emp_id = st.session_state.emp_id

    # =====================================================
    # LOAD EMPLOYEES
    # =====================================================

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

        if emp["emp_id"] != emp_id:

            employee_options.append(
                f"{emp['emp_name']} ({emp['emp_id']})"
            )

    if not employee_options:

        st.warning(
            "No employees available"
        )

        return

    # =====================================================
    # REQUEST SWAP
    # =====================================================

    st.subheader("Request Shift Swap")

    selected = st.selectbox(
        "Select Employee",
        employee_options
    )

    target_emp_id = (
        selected.split("(")[1]
        .replace(")", "")
        .strip()
    )

    shift_date = st.date_input(
        "Shift Date",
        value=date.today()
    )

    if st.button(
        "Request Shift Swap",
        width="stretch"
    ):

        response = requests.post(

            f"{API}/api/v1/swap/request",

            json={

                "requester_emp_id":
                emp_id,

                "target_emp_id":
                target_emp_id,

                "shift_date":
                str(shift_date)

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
                "Backend Error"
            )

    st.divider()

    # =====================================================
    # INCOMING REQUESTS
    # =====================================================

    st.subheader("Incoming Requests")

    try:

        incoming_response = requests.get(
            f"{API}/api/v1/swap/incoming/{emp_id}"
        )

        if incoming_response.status_code == 200:

            incoming = incoming_response.json()

            if incoming:

                for item in incoming:

                    with st.container():

                        st.info(

                            f"""
Requester: {item['requester_name']}

Date: {item['date']}

Their Shift: {item['their_shift']}

Your Shift: {item['your_shift']}

Status: {item['status']}
"""
                        )

                        if item["status"] == "Pending":

                            col1, col2 = st.columns(2)

                            with col1:

                                if st.button(

                                    f"Approve {item['swap_id']}",

                                    width="stretch"

                                ):

                                    approve = requests.put(

                                        f"{API}/api/v1/swap/approve/{item['swap_id']}"

                                    )

                                    if approve.status_code == 200:

                                        st.success(
                                            "Swap Approved"
                                        )

                                        st.rerun()

                                    else:

                                        st.error(
                                            "Approval Failed"
                                        )

                            with col2:

                                if st.button(

                                    f"Reject {item['swap_id']}",

                                    width="stretch"

                                ):

                                    reject = requests.put(

                                        f"{API}/api/v1/swap/reject/{item['swap_id']}"

                                    )

                                    if reject.status_code == 200:

                                        st.error(
                                            "Swap Rejected"
                                        )

                                        st.rerun()

                                    else:

                                        st.error(
                                            "Rejection Failed"
                                        )

                        st.divider()

            else:

                st.info(
                    "No incoming requests"
                )

    except Exception as e:

        st.error(str(e))

    st.divider()

    # =====================================================
    # SWAP HISTORY
    # =====================================================

    st.subheader("My Swap Requests")

    try:

        history_response = requests.get(
            f"{API}/api/v1/swap/my-requests/{emp_id}"
        )

        if history_response.status_code == 200:

            history = history_response.json()

            if history:

                for item in history:

                    status = item["status"]

                    message = f"""
Request To: {item['target_employee']}

Date: {item['date']}

Your Shift: {item['your_shift']}

Requested Shift: {item['target_shift']}

Status: {status}
"""

                    if status == "Approved":

                        st.success(message)

                    elif status == "Rejected":

                        st.error(message)

                    else:

                        st.warning(message)

            else:

                st.info(
                    "No swap requests"
                )

        else:

            st.error(
                "Failed to load history"
            )

    except Exception as e:

        st.error(str(e))
