import streamlit as st
import requests

API = "http://127.0.0.1:8000"


def show_admin_reset_password():

    st.title("Admin Reset Password")

    emp_id = st.text_input(
        "Employee ID"
    )

    new_password = st.text_input(
        "New Password",
        type="password"
    )

    if st.button(
        "Reset Password",
        width="stretch"
    ):

        try:

            response = requests.post(

                f"{API}/api/v1/auth/admin-reset-password",

                json={

                    "emp_id": emp_id,

                    "new_password": new_password

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

        except Exception as e:

            st.error(str(e))