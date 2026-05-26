import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000/api/v1"

st.title("CHANGE PASSWORD")

old_password = st.text_input(
    "Old Password",
    type="password"
)

new_password = st.text_input(
    "New Password",
    type="password"
)

if st.button("UPDATE PASSWORD"):

    response = requests.post(
        f"{BASE_URL}/auth/change-password",
        json={
            "employee_id":
            st.session_state["emp_id"],

            "old_password":
            old_password,

            "new_password":
            new_password
        }
    )

    if response.status_code == 200:

        st.success(
            "Password Updated"
        )

    else:

        st.error(
            response.json()["detail"]
        )