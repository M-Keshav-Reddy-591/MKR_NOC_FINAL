import streamlit as st

from utils.api import login_user
from utils.auth import save_login
from utils.sidebar import (
    admin_sidebar,
    employee_sidebar
)

st.set_page_config(
    page_title="NOC Attendance System",
    layout="wide"
)

# LOGIN CHECK

if "token" not in st.session_state:

    st.title("NOC ATTENDANCE SYSTEM")

    role = st.selectbox(
        "Select Role",
        ["admin", "employee"]
    )

    emp_id = st.text_input(
        "Employee ID"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("LOGIN"):

        response = login_user(
            emp_id,
            password,
            role
        )

        if response.status_code == 200:

            data = response.json()

            save_login(data)

            st.success("Login Successful")

            st.rerun()

        else:

            st.error(
                response.json()["detail"]
            )

else:

    role = st.session_state["role"]

    st.title(
        f"Welcome {st.session_state['emp_name']}"
    )

    if role == "admin":

        selected = admin_sidebar()

        if selected == "Dashboard":
            st.switch_page(
                "pages/admin_dashboard.py"
            )

        elif selected == "Employees":
            st.switch_page(
                "pages/attendance.py"
            )

        elif selected == "Shift Management":
            st.switch_page(
                "pages/shift_management.py"
            )

        elif selected == "CSV Upload":
            st.switch_page(
                "pages/csv_upload.py"
            )

        elif selected == "Analytics":
            st.switch_page(
                "pages/analytics.py"
            )

        elif selected == "Reports":
            st.switch_page(
                "pages/reports.py"
            )

        elif selected == "Change Password":
            st.switch_page(
                "pages/change_password.py"
            )

    else:

        selected = employee_sidebar()

        if selected == "Dashboard":
            st.switch_page(
                "pages/employee_dashboard.py"
            )

        elif selected == "Mark Attendance":
            st.switch_page(
                "pages/attendance.py"
            )

        elif selected == "Change Password":
            st.switch_page(
                "pages/change_password.py"
            )