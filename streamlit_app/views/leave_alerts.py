import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


def show_leave_alerts():

    st.title("Leave Alerts")

    response = requests.get(
        f"{API_URL}/api/v1/leaves/"
    )

    if response.status_code != 200:

        st.error(
            "Unable to fetch leave alerts"
        )

        return

    leaves = response.json()

    if not leaves:

        st.info(
            "No leave requests found"
        )

        return

    for index, leave in enumerate(leaves):

        with st.container():

            st.subheader(
                leave["employee_name"]
            )

            st.write(
                f"Employee ID: {leave['employee_id']}"
            )

            st.write(
                f"Date: {leave['date']}"
            )

            st.write(
                f"Shift: {leave['shift_name']}"
            )

            st.write(
                f"Leave Type: {leave['leave_type']}"
            )

            st.write(
                f"Reason: {leave['reason']}"
            )

            st.write(
                f"Status: {leave['status']}"
            )

            col1, col2 = st.columns(2)

            # ============================================
            # APPROVE
            # ============================================

            if leave["status"] == "Pending":

                with col1:

                    if st.button(

                        "Approve",

                        key=f"approve_{index}"

                    ):

                        requests.put(

                            f"{API_URL}/api/v1/leaves/update-status",

                            json={

                                "employee_id": leave["employee_id"],

                                "leave_date": leave["date"],

                                "shift_name": leave["shift_name"],

                                "status": "Approved"

                            }

                        )

                        st.rerun()

                # ============================================
                # REJECT
                # ============================================

                with col2:

                    if st.button(

                        "Reject",

                        key=f"reject_{index}"

                    ):

                        requests.put(

                            f"{API_URL}/api/v1/leaves/update-status",

                            json={

                                "employee_id": leave["employee_id"],

                                "leave_date": leave["date"],

                                "shift_name": leave["shift_name"],

                                "status": "Rejected"

                            }

                        )

                        st.rerun()

            st.divider()