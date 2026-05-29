import streamlit as st
import requests

API = "http://127.0.0.1:8000"


def show_edit_employees():

    st.title("Edit Employees")

    response = requests.get(
        f"{API}/api/v1/employees"
    )

    if response.status_code != 200:

        st.error(
            "Failed to load employees"
        )

        return

    employees = response.json()

    employee_map = {}

    for emp in employees:

        employee_map[
            f"{emp['emp_id']} - {emp['emp_name']}"
        ] = emp

    selected = st.selectbox(
        "Select Employee",
        list(employee_map.keys())
    )

    employee = employee_map[selected]

    emp_name = st.text_input(
        "Employee Name",
        value=employee["emp_name"]
    )

    department = st.text_input(
        "Department",
        value=employee["department"]
    )

    designation = st.text_input(
        "Designation",
        value=employee["designation"]
    )

    phone = st.text_input(
        "Phone Number",
        value=employee.get(
            "phone_number",
            ""
        )
    )

    email = st.text_input(
        "Email",
        value=employee.get(
            "email",
            ""
        )
    )

    role = st.selectbox(
        "Role",
        ["admin", "employee"],
        index=0 if employee["role"] == "admin" else 1
    )

    if st.button(
        "Update Employee",
        width="stretch"
    ):

        response = requests.put(

            f"{API}/api/v1/employees/update/{employee['emp_id']}",

            json={

                "emp_name": emp_name,

                "department": department,

                "designation": designation,

                "phone_number": phone,

                "email": email,

                "role": role

            }

        )

        if response.status_code == 200:

            st.success(
                "Employee updated successfully"
            )

        else:

            st.error(
                "Update failed"
            )
