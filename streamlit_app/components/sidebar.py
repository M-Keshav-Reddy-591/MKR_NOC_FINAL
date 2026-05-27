import streamlit as st


def admin_sidebar():

    with st.sidebar:

        st.title("ADMIN PANEL")

        if st.button(
            "Dashboard",
            width="stretch"
        ):
            st.session_state.page = "dashboard"

        if st.button(
            "Employees",
            width="stretch"
        ):
            st.session_state.page = "employees"

        if st.button(
            "Shifts",
            width="stretch"
        ):
            st.session_state.page = "shifts"

        if st.button(
            "Manual Attendance",
            width="stretch"
        ):
            st.session_state.page = "manual_attendance"

        if st.button(
            "Reports",
            width="stretch"
        ):
            st.session_state.page = "reports"

        if st.button(
            "Change Password",
            width="stretch"
        ):
            st.session_state.page = "change_password"

        st.divider()

        if st.button(
            "Logout",
            width="stretch"
        ):

            st.session_state.clear()

            st.rerun()


def employee_sidebar():

    with st.sidebar:

        st.title("EMPLOYEE")

        st.write(
            f"Welcome {st.session_state.get('emp_name')}"
        )

        if st.button(
            "Dashboard",
            width="stretch"
        ):
            st.session_state.page = "dashboard"

        if st.button(
            "Attendance",
            width="stretch"
        ):
            st.session_state.page = "attendance"

        if st.button(
            "Change Password",
            width="stretch"
        ):
            st.session_state.page = "change_password"

        st.divider()

        if st.button(
            "Logout",
            width="stretch"
        ):

            st.session_state.clear()

            st.rerun()