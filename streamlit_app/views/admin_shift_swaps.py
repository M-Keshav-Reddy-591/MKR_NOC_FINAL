import streamlit as st
import requests

API = "http://127.0.0.1:8000/api/v1"


def show_admin_shift_swaps():

    st.title("Shift Swap Requests")

    try:

        response = requests.get(
            f"{API}/swap/all"
        )

        if response.status_code != 200:

            st.error(
                "Failed to load swaps"
            )

            return

        swaps = response.json()

        if not swaps:

            st.info(
                "No shift swaps found"
            )

            return

        for swap in swaps:

            with st.container(border=True):

                st.subheader(
                    f"{swap['requester']} → {swap['target']}"
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

                st.write(
                    f"Status: {swap['status']}"
                )

                if swap["status"] == "Pending":

                    col1, col2 = st.columns(2)

                    with col1:

                        if st.button(
                            f"Approve {swap['swap_id']}"
                        ):

                            requests.put(
                                f"{API}/swap/approve/{swap['swap_id']}"
                            )

                            st.success(
                                "Swap approved"
                            )

                            st.rerun()

                    with col2:

                        if st.button(
                            f"Reject {swap['swap_id']}"
                        ):

                            requests.put(
                                f"{API}/swap/reject/{swap['swap_id']}"
                            )

                            st.error(
                                "Swap rejected"
                            )

                            st.rerun()

    except Exception as e:

        st.error(str(e))