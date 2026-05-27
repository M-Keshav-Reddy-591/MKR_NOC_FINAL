import streamlit as st
import requests

from views.admin_dashboard import show_admin_dashboard
from views.employees import show_employees
from views.attendance import show_attendance
from views.shifts import show_shifts
from views.analytics import show_analytics
from views.reports import show_reports
from views.csv_upload import show_csv_upload
from views.change_password import show_change_password

API = "http://127.0.0.1:8000/api/v1"

st.set_page_config(
    page_title="NOC Attendance",
    layout="wide"
)

# ---------------- SESSION ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = ""

if "employee" not in st.session_state:
    st.session_state.employee = {}

# ---------------- LOGIN SCREEN ----------------

if not st.session_state.logged_in:

    st.title("NOC Attendance Login")

    emp_id = st.text_input("Employee ID")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        payload = {
            "emp_id": emp_id,
            "password": password
        }

        try:

            response = requests.post(
                f"{API}/auth/login",
                json=payload
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state.logged_in = True
                st.session_state.role = data["employee"]["role"]
                st.session_state.employee = data["employee"]

                st.rerun()

            else:

                st.error(
                    response.json()["detail"]
                )

        except Exception as e:

            st.error(str(e))

# ---------------- AFTER LOGIN ----------------

else:

    st.sidebar.title("NOC Attendance")

    st.sidebar.write(
        f"Welcome {st.session_state.employee['name']}"
    )

    role = st.session_state.role

    # ADMIN MENU

    if role == "admin":

        menu = st.sidebar.radio(

            "Navigation",

            [
                "Dashboard",
                "Employees",
                "Attendance",
                "Shifts",
                "Analytics",
                "Reports",
                "CSV Upload",
                "Change Password"
            ]
        )

    # EMPLOYEE MENU

    else:

        menu = st.sidebar.radio(

            "Navigation",

            [
                "Attendance",
                "Shifts",
                "Change Password"
            ]
        )

    # LOGOUT

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.role = ""
        st.session_state.employee = {}

        st.rerun()

    # PAGE RENDERING

    if menu == "Dashboard":
        show_admin_dashboard()

    elif menu == "Employees":
        show_employees()

    elif menu == "Attendance":
        show_attendance()

    elif menu == "Shifts":
        show_shifts()

    elif menu == "Analytics":
        show_analytics()

    elif menu == "Reports":
        show_reports()

    elif menu == "CSV Upload":
        show_csv_upload()

    elif menu == "Change Password":
        show_change_password()