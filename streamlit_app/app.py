import streamlit as st
import requests

from components.sidebar import (
    admin_sidebar,
    employee_sidebar
)

from views.admin_dashboard import admin_dashboard
from views.employees import employees
from views.shifts import shifts
from views.manual_attendance import manual_attendance
from views.reports import reports
from views.change_password import change_password
from views.employee_dashboard import employee_dashboard
from views.employee_attendance import employee_attendance


# ==========================================
# SESSION INIT
# ==========================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "role" not in st.session_state:

    st.session_state.role = ""

if "emp_name" not in st.session_state:

    st.session_state.emp_name = ""

if "emp_id" not in st.session_state:

    st.session_state.emp_id = ""


# ==========================================
# LOGIN PAGE
# ==========================================

if not st.session_state.logged_in:

    st.set_page_config(
        page_title="NOC Attendance",
        layout="wide"
    )

    st.title("NOC Attendance Login")

    role = st.selectbox(

        "Role",

        [
            "admin",
            "employee"
        ]

    )

    emp_id = st.text_input(
        "Employee ID"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        response = requests.post(

            "http://127.0.0.1:8000/api/v1/auth/login",

            json={

                "emp_id": emp_id,
                "password": password,
                "role": role

            }

        )

        data = response.json()

        if response.status_code == 200:

            st.session_state.logged_in = True

            st.session_state.role = data["employee"]["role"]

            st.session_state.emp_name = data["employee"]["name"]

            st.session_state.emp_id = data["employee"]["emp_id"]

            st.rerun()

        else:

            st.error(
                data["detail"]
            )


# ==========================================
# ADMIN PANEL
# ==========================================

elif st.session_state.role == "admin":

    selected = admin_sidebar()

    if selected == "Dashboard":

        show_admin_dashboard()

    elif selected == "Employees":

        show_employees()

    elif selected == "Shifts":

        show_shifts()

    elif selected == "Manual Attendance":

        show_manual_attendance()

    elif selected == "Reports":

        show_reports()

    elif selected == "Change Password":

        show_change_password()


# ==========================================
# EMPLOYEE PANEL
# ==========================================

else:

    selected = employee_sidebar()

    if selected == "Dashboard":

        show_employee_dashboard()

    elif selected == "Attendance":

        show_employee_attendance()

    elif selected == "Change Password":

        show_change_password()