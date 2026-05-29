import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"


def show_leave_alerts():

    st.title("Leave Alerts")

    response = requests.get(
        f"{API}/api/v1/leaves/"
    )

    if response.status_code == 200:

        data = response.json()

        if data:

            for leave in data:

                with st.container():

                    st.subheader(
                        leave["employee_name"]
                    )

                    st.write(
                        f"Employee ID: {leave['employee_id']}"
                    )

                    st.write(
                        f"Date: {leave['leave_date']}"
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

                    with col1:

                        if st.button(
                            f"Approve {leave['id']}"
                        ):

                            requests.put(

                                f"{API}/api/v1/leaves/approve/{leave['id']}"
                            )

                            st.rerun()

                    with col2:

                        if st.button(
                            f"Reject {leave['id']}"
                        ):

                            requests.put(

                                f"{API}/api/v1/leaves/reject/{leave['id']}"
                            )

                            st.rerun()

                    st.divider()

        else:

            st.warning(
                "No leave requests found"
            )