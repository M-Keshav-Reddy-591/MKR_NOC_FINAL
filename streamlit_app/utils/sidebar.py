import streamlit as st
from streamlit_option_menu import option_menu


def admin_sidebar():

    with st.sidebar:

        selected = option_menu(
            "ADMIN PANEL",
            [
                "Dashboard",
                "Employees",
                "Attendance",
                "Shift Management",
                "CSV Upload",
                "Analytics",
                "Reports",
                "Change Password",
                "Logout"
            ],
            icons=[
                "speedometer2",
                "people",
                "calendar-check",
                "clock-history",
                "upload",
                "bar-chart",
                "file-earmark",
                "key",
                "box-arrow-right"
            ],
            menu_icon="shield-lock",
            default_index=0
        )

    return selected


def employee_sidebar():

    with st.sidebar:

        selected = option_menu(
            "EMPLOYEE PANEL",
            [
                "Dashboard",
                "Mark Attendance",
                "Upcoming Shifts",
                "Shift History",
                "Reports",
                "Change Password",
                "Logout"
            ],
            icons=[
                "speedometer2",
                "calendar-check",
                "clock",
                "clock-history",
                "file-earmark",
                "key",
                "box-arrow-right"
            ],
            menu_icon="person-circle",
            default_index=0
        )

    return selected