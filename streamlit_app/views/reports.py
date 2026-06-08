# import streamlit as st
# import requests
# import pandas as pd

# API = "http://127.0.0.1:8000"

# def show_reports():

#     st.title("Attendance Reports")

#     response = requests.get(
#         f"{API}/api/v1/reports/all"
#     )

#     if response.status_code == 200:

#         data = response.json()

#         if data:

#             df = pd.DataFrame(data)

#             st.dataframe(
#                 df,
#                 width="stretch"
#             )

#             csv = df.to_csv(
#                 index=False
#             ).encode("utf-8")

#             st.download_button(
#                 "Download CSV",
#                 csv,
#                 "attendance_report.csv",
#                 "text/csv",
#                 width="stretch"
#             )

#         else:

#             st.warning(
#                 "No attendance records found"
#             )

#     else:

#         st.error(
#             "Failed to load reports"
#         )
import streamlit as st
import requests
import pandas as pd
from datetime import datetime

API_URL = "http://127.0.0.1:8000"


def show_reports():

    st.title("Reports")

    report_type = st.selectbox(

        "Select Report",

        [

            "Monthly Attendance Summary",

            "Absent Employees",

            "Employee Attendance History",

            "All Attendance Records"

        ]

    )

    # current_year = datetime.now().year

    # month = st.selectbox(

    #     "Month",

    #     list(range(1, 13)),

    #     index=datetime.now().month - 1

    # )

    # year = st.selectbox(

    #     "Year",

    #     [2024, 2025, 2026, 2027],

    #     index=2

    # )

    # =====================================================
    # AVAILABLE YEARS & MONTHS FROM DATABASE
    # =====================================================

    periods_response = requests.get(
        f"{API_URL}/api/v1/reports/available-periods"
    )

    periods = periods_response.json()

    available_years = list(
        periods.keys()
    )

    selected_year = st.selectbox(
        "Year",
        available_years
    )

    available_months = periods[
        selected_year
    ]

    month_names = {

        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"

    }

    month_display = {

        month_names[m]: m

        for m in available_months

    }

    selected_month = st.selectbox(

        "Month",

        list(month_display.keys())

    )

    month = month_display[
        selected_month
    ]

    year = int(
        selected_year
    )

    st.divider()

    # =====================================================
    # MONTHLY SUMMARY
    # =====================================================

    if report_type == "Monthly Attendance Summary":

        if st.button(
            "Generate Report",
            width="stretch"
        ):

            response = requests.get(

                f"{API_URL}/api/v1/reports/monthly",

                params={

                    "month": month,

                    "year": year

                }

            )

            if response.status_code == 200:

                data = response.json()

                df = pd.DataFrame(data)

                st.dataframe(
                    df,
                    width="stretch"
                )

                csv = df.to_csv(
                    index=False
                )

                st.download_button(

                    "Download CSV",

                    csv,

                    file_name=f"monthly_report_{month}_{year}.csv",

                    mime="text/csv"

                )

    # =====================================================
    # ABSENT REPORT
    # =====================================================

    elif report_type == "Absent Employees":

        if st.button(
            "Generate Report",
            width="stretch"
        ):

            response = requests.get(

                f"{API_URL}/api/v1/reports/absent",

                params={

                    "month": month,

                    "year": year

                }

            )

            if response.status_code == 200:

                data = response.json()

                df = pd.DataFrame(data)

                st.dataframe(
                    df,
                    width="stretch"
                )

                csv = df.to_csv(
                    index=False
                )

                st.download_button(

                    "Download CSV",

                    csv,

                    file_name=f"absent_report_{month}_{year}.csv",

                    mime="text/csv"

                )

    # =====================================================
    # EMPLOYEE REPORT
    # =====================================================

    elif report_type == "Employee Attendance History":

        employees = requests.get(

            f"{API_URL}/api/v1/employees"

        ).json()

        employee_map = {

            f"{e['emp_name']} ({e['emp_id']})":
            e["emp_id"]

            for e in employees

        }

        selected = st.selectbox(

            "Select Employee",

            list(employee_map.keys())

        )

        emp_id = employee_map[selected]

        if st.button(
            "Generate Report",
            width="stretch"
        ):

            response = requests.get(

                f"{API_URL}/api/v1/reports/employee/{emp_id}"

            )

            if response.status_code == 200:

                data = response.json()

                df = pd.DataFrame(data)

                st.dataframe(
                    df,
                    width="stretch"
                )

                csv = df.to_csv(
                    index=False
                )

                st.download_button(

                    "Download CSV",

                    csv,

                    file_name=f"{emp_id}_attendance.csv",

                    mime="text/csv"

                )

    # =====================================================
    # ALL ATTENDANCE
    # =====================================================

    elif report_type == "All Attendance Records":

        if st.button(
            "Generate Report",
            width="stretch"
        ):

            response = requests.get(

                f"{API_URL}/api/v1/reports/all"

            )

            if response.status_code == 200:

                data = response.json()

                df = pd.DataFrame(data)

                st.dataframe(
                    df,
                    width="stretch"
                )

                csv = df.to_csv(
                    index=False
                )

                st.download_button(

                    "Download CSV",

                    csv,

                    file_name="attendance_report.csv",

                    mime="text/csv"

                )