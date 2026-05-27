import streamlit as st


# ==========================================
# ADMIN SIDEBAR
# ==========================================

def admin_sidebar():

    with st.sidebar:

        st.markdown("# 🛡️ ADMIN PANEL")

        st.caption("NOC Attendance Management")

        st.divider()

        selected = st.radio(

            "Navigation",

            [

                "Dashboard",
                "Employees",
                "Shifts",
                "Manual Attendance",
                "Reports",
                "Change Password"

            ]

        )

        st.divider()

        if st.button(
            "🚪 Logout",
            width="stretch"
        ):

            st.session_state.clear()

            st.rerun()

        return selected


# ==========================================
# EMPLOYEE SIDEBAR
# ==========================================

def employee_sidebar():

    with st.sidebar:

        st.title("NOC Attendance")

        st.write(

            f"Welcome {st.session_state.get('emp_name', '')}"

        )

        st.divider()

        selected = st.radio(

            "Navigation",

            [

                "Dashboard",
                "Attendance",
                "Change Password"

            ]

        )

        st.divider()

        if st.button(
            "Logout",
            width="stretch"
        ):

            st.session_state.clear()

            st.rerun()

        return selected