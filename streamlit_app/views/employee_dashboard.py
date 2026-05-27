import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"

employee_name = st.session_state.get(
    "emp_name"
)

employee_id = st.session_state.get(
    "employee_id"
)

st.title(
    f"Welcome {employee_name}"
)

st.subheader(
    "Upcoming Shifts"
)

response = requests.get(
    f"{API}/api/v1/shifts/"
)

if response.status_code == 200:

    shifts = response.json()

    employee_shifts = []

    for shift in shifts:

        if shift["employee_id"] == employee_id:

            employee_shifts.append(shift)

    if len(employee_shifts) > 0:

        df = pd.DataFrame(
            employee_shifts
        )

        st.dataframe(
            df,
            width="stretch"
        )

    else:

        st.info(
            "No upcoming shifts"
        )

else:

    st.error(
        "Unable to fetch shifts"
    )