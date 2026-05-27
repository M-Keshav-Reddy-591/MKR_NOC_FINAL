import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000/api/v1"

def show_employees():

    st.title("Employee Management")

    # ==========================
    # ADD EMPLOYEE FORM
    # ==========================

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

    with col2:

        designation = st.text_input(
            "Designation"
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

    # ==========================
    # REGISTER BUTTON
    # ==========================

    if st.button("Add Employee"):

        payload = {

            "emp_id": emp_id,
            "emp_name": emp_name,
            "department": department,
            "designation": designation,
            "role": role,
            "password": password
        }

        try:

            response = requests.post(

                f"{API}/auth/register",

                json=payload
            )

            if response.status_code == 200:

                st.success(
                    "Employee Added Successfully"
                )

            else:

                st.error(
                    response.json()["detail"]
                )

        except Exception as e:

            st.error(str(e))

    st.divider()

    # ==========================
    # EMPLOYEE TABLE
    # ==========================

    st.subheader("Employee List")

    try:

        response = requests.get(
            f"{API}/employees"
        )

        data = response.json()

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            width="stretch"
        )

    except Exception as e:

        st.error(str(e))