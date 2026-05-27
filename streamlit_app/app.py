import streamlit as st

from utils.styles import load_css
from utils.sidebar import admin_sidebar

from views.admin_dashboard import show_admin_dashboard
from views.employees import show_employees
from views.attendance import show_attendance
from views.shifts import show_shifts
from views.analytics import show_analytics
from views.reports import show_reports
from views.csv_upload import show_csv_upload
from views.change_password import show_change_password

st.set_page_config(
    page_title="NOC Attendance",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_css()

menu = admin_sidebar()

if menu == "Dashboard":

    show_admin_dashboard()

elif menu == "Employees":

    show_employees()

elif menu == "Attendance":

    show_attendance()

elif menu == "Shift Management":

    show_shifts()

elif menu == "Analytics":

    show_analytics()

elif menu == "CSV Upload":

    show_csv_upload()

elif menu == "Reports":

    show_reports()

elif menu == "Change Password":

    show_change_password()