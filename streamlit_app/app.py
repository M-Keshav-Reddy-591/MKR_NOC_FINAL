import streamlit as st
import requests

from components.sidebar import (
    admin_sidebar,
    employee_sidebar
)

from views.edit_employees import (
    show_edit_employees
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
from views.apply_leave import (
    show_apply_leave
)
from views.password_logs import (
    show_password_logs
)

from views.notifications import (
    show_notifications
)

from views.shift_swap import (
    show_shift_swap
)

from views.swap_alerts import (
    show_swap_alerts
)
from views.admin_shift_swaps import (
    show_admin_shift_swaps
)
from views.leave_alerts import (
    show_leave_alerts
)
from views.admin_notifications import (
    show_admin_notifications
)
# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NOC Attendance",
    layout="wide"
)

# =========================================================
# SESSION DEFAULTS
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = ""

if "page" not in st.session_state:
    st.session_state.page = "dashboard"

if "emp_id" not in st.session_state:
    st.session_state.emp_id = ""

if "emp_name" not in st.session_state:
    st.session_state.emp_name = ""

# =========================================================
# LOGIN SCREEN
# =========================================================

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

        try:

            response = requests.post(
                "http://127.0.0.1:8000/api/v1/auth/login",
                json={
                    "emp_id": emp_id,
                    "password": password,
                    "role": role
                }
            )

            # SUCCESS LOGIN

            if response.status_code == 200:

                data = response.json()

                # BACKEND RESPONSE
                # data["employee"]

                employee = data.get("employee")

                if not employee:

                    st.error(
                        "Employee data missing from backend response"
                    )

                else:

                    st.session_state.logged_in = True

                    st.session_state.role = employee.get(
                        "role",
                        ""
                    )

                    st.session_state.emp_id = employee.get(
                        "emp_id",
                        ""
                    )

                    st.session_state.emp_name = employee.get(
                        "name",
                        ""
                    )

                    # DEFAULT PAGE

                    st.session_state.page = "dashboard"

                    st.rerun()

            # FAILED LOGIN

            else:

                try:

                    st.error(
                        response.json()["detail"]
                    )

                except:

                    st.error(
                        response.text
                    )

        except Exception as e:

            st.error(
                f"Server Error : {str(e)}"
            )

# =========================================================
# ADMIN PANEL
# =========================================================

elif st.session_state.role == "admin":

    admin_sidebar()

    page = st.session_state.page

    if page == "dashboard":

        show_admin_dashboard()

    elif page == "employees":

        show_employees()
    
    elif st.session_state.page == "edit_employees":

        show_edit_employees()
    elif page == "admin_shift_swaps":

        show_admin_shift_swaps()


    # elif st.session_state.page == "swap_alerts":

    #     show_swap_alerts()



    elif page == "shifts":

        show_shifts()

    elif page == "manual_attendance":

        show_manual_attendance()

    elif page == "reports":

        show_reports()
    elif page == "leave_alerts":
        show_leave_alerts()
    elif st.session_state.page == "password_logs":

        show_password_logs()

    elif st.session_state.page == "admin_notifications":


        show_admin_notifications()

    elif page == "change_password":

        show_change_password()

# =========================================================
# EMPLOYEE PANEL
# =========================================================

elif st.session_state.role == "employee":

    employee_sidebar()

    page = st.session_state.page

    if page == "dashboard":

        show_employee_dashboard()

    elif page == "attendance":

        show_employee_attendance()

    elif page == "apply_leave":

        show_apply_leave()

    elif st.session_state.page == "shift_swap":

        show_shift_swap()

    elif page == "change_password":

        show_change_password()

# =========================================================
# INVALID ROLE SAFETY
# =========================================================

else:

    st.error(
        "Invalid role detected"
    )

    st.session_state.clear()

    st.rerun()