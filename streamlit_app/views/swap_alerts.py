import streamlit as st
import requests

API = "http://127.0.0.1:8000"


def show_swap_alerts():

    st.title("Shift Swap Requests")

    response = requests.get(
        f"{API}/api/v1/swaps/"
    )

    if response.status_code != 200:

        st.error(
            "Failed to load swaps"
        )

        return

    swaps = response.json()

    pending_found = False

    for swap in swaps:

        if swap["status"] == "Pending":

            pending_found = True

            with st.container(border=True):

                st.subheader(
                    swap["requester_name"]
                )

                st.write(
                    f"Requester ID: {swap['requester_emp_id']}"
                )

                st.write(
                    f"Target Employee: {swap['target_name']}"
                )

                st.write(
                    f"Date: {swap['date']}"
                )

                st.write(
                    f"Requester Shift: {swap['requester_shift']}"
                )

                st.write(
                    f"Target Shift: {swap['target_shift']}"
                )

                col1, col2 = st.columns(2)

                with col1:

                    if st.button(

                        "Approve",

                        key=f"approve_{swap['swap_id']}",

                        width="stretch"

                    ):

                        requests.put(
                            f"{API}/api/v1/swaps/approve/{swap['swap_id']}"
                        )

                        st.success(
                            "Approved"
                        )

                        st.rerun()

                with col2:

                    if st.button(

                        "Reject",

                        key=f"reject_{swap['swap_id']}",

                        width="stretch"

                    ):

                        requests.put(
                            f"{API}/api/v1/swaps/reject/{swap['swap_id']}"
                        )

                        st.success(
                            "Rejected"
                        )

                        st.rerun()

    if not pending_found:

        st.info(
            "No pending shift swaps"
        )
