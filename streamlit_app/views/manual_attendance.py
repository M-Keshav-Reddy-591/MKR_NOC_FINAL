# import streamlit as st
# import requests
# import pandas as pd
# from datetime import date


# API_URL = "http://127.0.0.1:8000"


# def show_manual_attendance():

#     st.title("Manual Attendance")

#     # =====================================================
#     # EMPLOYEE
#     # =====================================================

#     # employee_id = st.text_input(
#     #     "Employee ID"
#     # )
#     emp_response = requests.get(
#         f"{API_URL}/api/v1/employees"
#     )

#     employees = emp_response.json()

#     employee_map = {

#         f"{e['emp_name']} ({e['emp_id']})":
#         e["emp_id"]

#         for e in employees

#     }

#     selected = st.selectbox(

#         "Select Employee",

#         list(employee_map.keys())

#     )

#     employee_id = employee_map[selected]

#     summary = requests.get(

#         f"{API_URL}/api/v1/attendance/employee-summary/{employee_id}"

#     ).json()

#     emp = summary["employee"]

#     st.info(

#         f"""
#     Name : {emp['emp_name']}

#     Department : {emp['department']}

#     Designation : {emp['designation']}

#     Role : {emp['role']}
#     """
#     )

#     st.subheader(
#         "Assigned Shifts"
#     )

#     shift_df = pd.DataFrame(
#         summary["shifts"]
#     )

#     st.dataframe(
#         shift_df,
#         width="stretch"
#     )

#     st.subheader(
#         "Attendance History"
#     )

#     attendance_df = pd.DataFrame(
#         summary["attendance"]
#     )

#     st.dataframe(
#         attendance_df,
#         width="stretch"
#     )




#     attendance_date = st.date_input(
#         "Attendance Date",
#         value=date.today()
#     )

#     shifts = []

#     # =====================================================
#     # FETCH SHIFTS
#     # =====================================================

#     if employee_id:

#         response = requests.get(

#             f"{API_URL}/api/v1/shifts/{employee_id}/{attendance_date}"

#         )

#         if response.status_code == 200:

#             shifts = response.json()

#     shift_names = []

#     for shift in shifts:

#         if isinstance(shift, dict):

#             shift_names.append(
#                 shift["shift_name"]
#             )

#         else:

#             shift_names.append(
#                 shift
#             )

#     # =====================================================
#     # SHIFT SELECT
#     # =====================================================

#     if shift_names:

#         selected_shift = st.selectbox(
#             "Assigned Shift",
#             shift_names
#         )

#     else:

#         selected_shift = st.text_input(
#             "Shift Name"
#         )

#     # =====================================================
#     # STATUS
#     # =====================================================

#     status = st.selectbox(

#         "Attendance Status",

#         [
#             "Present",
#             "Absent",
#             "Leave"
#         ]

#     )

#     # =====================================================
#     # MARK ATTENDANCE
#     # =====================================================

#     if st.button(
#         "Mark Attendance",
#         width="stretch"
#     ):

#         payload = {

#             "employee_id": employee_id,

#             "attendance_date": str(
#                 attendance_date
#             ),

#             "shift_name": selected_shift,

#             "status": status

#         }

#         response = requests.post(

#             f"{API_URL}/api/v1/attendance/manual",

#             json=payload

#         )

#         if response.status_code == 200:

#             st.success(
#                 "Attendance marked successfully"
#             )

#         else:

#             try:

#                 st.error(
#                     response.json()["detail"]
#                 )

#             except:

#                 st.error(
#                     response.text
#                 )

#     st.divider()

#     # =====================================================
#     # ATTENDANCE LIST
#     # =====================================================

#     st.subheader(
#         "Attendance Records"
#     )

#     response = requests.get(
#         f"{API_URL}/api/v1/attendance/"
#     )

#     if response.status_code == 200:

#         data = response.json()

#         if data:

#             df = pd.DataFrame(data)

#             st.dataframe(
#                 df,
#                 width="stretch"
#             )

#         else:

#             st.info(
#                 "No attendance records found"
#             )
import streamlit as st
import requests
import pandas as pd
from datetime import date

# =====================================================
# CONFIG
# =====================================================

API_URL = "http://127.0.0.1:8000"

# =====================================================
# PAGE
# =====================================================

def show_manual_attendance():

    st.title("Manual Attendance")

    # =====================================================
    # LOAD EMPLOYEES
    # =====================================================

    try:

        emp_response = requests.get(
            f"{API_URL}/api/v1/employees"
        )

        if emp_response.status_code != 200:

            st.error("Failed to load employees")
            return

        employees = emp_response.json()

    except Exception as e:

        st.error(f"API Error : {str(e)}")
        return

    if not employees:

        st.warning("No employees found")
        return

    # =====================================================
    # EMPLOYEE DROPDOWN
    # =====================================================

    employee_map = {

        f"{emp['emp_name']} ({emp['emp_id']})":
        emp["emp_id"]

        for emp in employees

    }

    selected_employee = st.selectbox(
        "Select Employee",
        list(employee_map.keys())
    )

    employee_id = employee_map[selected_employee]

    # =====================================================
    # EMPLOYEE SUMMARY
    # =====================================================

    try:

        summary_response = requests.get(
            f"{API_URL}/api/v1/attendance/employee-summary/{employee_id}"
        )

        if summary_response.status_code != 200:

            st.error("Failed to load employee summary")
            return

        summary = summary_response.json()

    except Exception as e:

        st.error(str(e))
        return

    emp = summary["employee"]

    st.info(
        f"""
Name : {emp['emp_name']}

Department : {emp['department']}

Designation : {emp['designation']}

Role : {emp['role']}
"""
    )

    # =====================================================
    # ASSIGNED SHIFTS
    # =====================================================

    st.subheader("Assigned Shifts")

    shifts_data = summary.get(
        "shifts",
        []
    )

    if shifts_data:

        shift_df = pd.DataFrame(
            shifts_data
        )

        st.dataframe(
            shift_df,
            width="stretch"
        )

    else:

        st.warning(
            "No shifts assigned"
        )

    # =====================================================
    # ATTENDANCE HISTORY
    # =====================================================

    st.subheader(
        "Attendance History"
    )

    attendance_data = summary.get(
        "attendance",
        []
    )

    if attendance_data:

        attendance_df = pd.DataFrame(
            attendance_data
        )

        st.dataframe(
            attendance_df,
            width="stretch"
        )

    else:

        st.info(
            "No attendance history"
        )

    st.divider()

    # =====================================================
    # MARK ATTENDANCE
    # =====================================================

    st.subheader(
        "Mark Attendance"
    )

    attendance_date = st.date_input(
        "Attendance Date",
        value=date.today()
    )

    shift_response = requests.get(
        f"{API_URL}/api/v1/shifts/{employee_id}/{attendance_date}"
    )

    assigned_shifts = []

    if shift_response.status_code == 200:

        assigned_shifts = shift_response.json()

    shift_names = []

    for shift in assigned_shifts:

        if isinstance(shift, dict):

            shift_names.append(
                shift["shift_name"]
            )

        else:

            shift_names.append(
                shift
            )

    # =====================================================
    # NO SHIFT ASSIGNED
    # =====================================================

    if not shift_names:

        st.warning(
            "No shift assigned for selected date"
        )

    else:

        selected_shift = st.selectbox(
            "Assigned Shift",
            shift_names
        )

        status = st.selectbox(

            "Attendance Status",

            [
                "Present",
                "Absent",
                "Leave"
            ]

        )

        if st.button(
            "Mark Attendance",
            width="stretch"
        ):

            payload = {

                "employee_id":
                employee_id,

                "attendance_date":
                str(attendance_date),

                "shift_name":
                selected_shift,

                "status":
                status

            }

            response = requests.post(

                f"{API_URL}/api/v1/attendance/manual",

                json=payload

            )

            if response.status_code == 200:

                st.success(
                    "Attendance marked successfully"
                )

                st.rerun()

            else:

                try:

                    st.error(
                        response.json()["detail"]
                    )

                except:

                    st.error(
                        response.text
                    )

    st.divider()

    # =====================================================
    # ALL ATTENDANCE RECORDS
    # =====================================================

    st.subheader(
        "Attendance Records"
    )

    response = requests.get(
        f"{API_URL}/api/v1/attendance/"
    )

    if response.status_code == 200:

        records = response.json()

        if records:

            df = pd.DataFrame(
                records
            )

            st.dataframe(
                df,
                width="stretch"
            )

        else:

            st.info(
                "No attendance records found"
            )

    else:

        st.error(
            "Failed to load attendance records"
        )