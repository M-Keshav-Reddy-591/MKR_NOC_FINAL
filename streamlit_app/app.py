import streamlit as st

from components.sidebar import (
    admin_sidebar,
    employee_sidebar
)

from views.admin_dashboard import (
    show_admin_dashboard
)

from views.employees import (
    show_employees
)

from views.shifts import (
    show_shifts
)

from views.manual_attendance import (
    show_manual_attendance
)

from views.reports import (
    show_reports
)

from views.change_password import (
    show_change_password
)

from views.employee_dashboard import (
    show_employee_dashboard
)

from views.employee_attendance import (
    show_employee_attendance
)

st.set_page_config(
    page_title="NOC Attendance",
    layout="wide"
)

# SESSION DEFAULTS

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = ""

if "page" not in st.session_state:
    st.session_state.page = "login"

# LOGIN SCREEN

if not st.session_state.logged_in:

    st.title("NOC Attendance Login")

    emp_id = st.text_input(
        "Employee ID"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    role = st.selectbox(
        "Role",
        [
            "admin",
            "employee"
        ]
    )

    if st.button(
        "Login",
        width="stretch"
    ):

        import requests

        response = requests.post(
            "http://127.0.0.1:8000/api/v1/auth/login",
            json={
                "emp_id": emp_id,
                "password": password,
                "role": role
            }
        )

        if response.status_code == 200:

            data = response.json()

            employee = data["employee"]

            st.session_state.logged_in = True

            st.session_state.role = employee["role"]

            st.session_state.emp_id = employee["emp_id"]

            st.session_state.emp_name = employee["name"]

            st.rerun()

        else:

            st.error(
                response.json()["detail"]
            )

# ADMIN PANEL

elif st.session_state.role == "admin":

    admin_sidebar()

    page = st.session_state.page

    if page == "dashboard":
        show_admin_dashboard()

    elif page == "employees":
        show_employees()

    elif page == "shifts":
        show_shifts()

    elif page == "manual_attendance":
        show_manual_attendance()

    elif page == "reports":
        show_reports()

    elif page == "change_password":
        show_change_password()

# EMPLOYEE PANEL

elif st.session_state.role == "employee":

    employee_sidebar()

    page = st.session_state.page

    if page == "dashboard":
        show_employee_dashboard()

    elif page == "attendance":
        show_employee_attendance()

    elif page == "change_password":
        show_change_password()