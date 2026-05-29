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
            "✏️ Edit Employees",
            width="stretch"
        ):
            st.session_state.page = "edit_employees"


        if st.button(
            "Shifts",
            width="stretch"
        ):
            st.session_state.page = "shifts"

        if st.button(
            "📂 CSV Shift Upload",
            width="stretch"
        ):
            st.session_state.page = "upload_shift_csv"


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
            "🚨 Leave Alerts",
            width="stretch"
        ):
            st.session_state.page = "leave_alerts"

        if st.button(
            "🔐 Password Logs",
            width="stretch"
        ):
            st.session_state.page = "password_logs"

        if st.button(
            "🔔 Admin Notifications",
            width="stretch"
        ):
            st.session_state.page = "admin_notifications"
        
        if st.button(
            "🔄 Shift Swaps",
            width="stretch"
        ):
            st.session_state.page = "admin_shift_swaps"
                

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
            "📝 Apply Leave",
            width="stretch"
        ):
            st.session_state.page = "apply_leave"

        if st.button(
            "🔔 Notifications",
            width="stretch"
        ):
            st.session_state.page = "notifications"
        
        if st.button(
            "🔄 Shift Swap",
            width="stretch"
        ):
            st.session_state.page = "shift_swap"
        

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
