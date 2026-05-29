
import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000/api/v1"


def show_employees():

    st.title("Employee Management")

    # =====================================================
    # ADD NEW EMPLOYEE
    # =====================================================

    st.subheader("Add New Employee")

    col1, col2 = st.columns(2)

    with col1:

        emp_id = st.text_input(
            "Employee ID"
        )

        emp_name = st.text_input(
            "Employee Name"
        )

        department = st.text_input(
            "Department"
        )

        phone_number = st.text_input(
            "Phone Number"
        )

    with col2:

        designation = st.text_input(
            "Designation"
        )

        email = st.text_input(
            "Email"
        )

        role = st.selectbox(
            "Role",
            [
                "employee",
                "admin"
            ]
        )

        password = st.text_input(
            "Password",
            type="password"
        )

    # =====================================================
    # ADD EMPLOYEE BUTTON
    # =====================================================

    if st.button(
        "Add Employee",
        width="stretch"
    ):

        payload = {

            "emp_id": emp_id,

            "emp_name": emp_name,

            "department": department,

            "designation": designation,

            "phone_number": phone_number,

            "email": email,

            "role": role,

            "password": password
        }

        try:

            response = requests.post(
                f"{API}/auth/register",
                json=payload
            )

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

        except Exception as e:

            st.error(str(e))

    st.divider()

    # =====================================================
    # EMPLOYEE LIST
    # =====================================================

    st.subheader("Employee List")

    try:

        response = requests.get(
            f"{API}/employees"
        )

        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(data)

            st.dataframe(
                df,
                width="stretch"
            )

        else:

            st.error(
                "Failed to load employees"
            )

    except Exception as e:

        st.error(str(e))
