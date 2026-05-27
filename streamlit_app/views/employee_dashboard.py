import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"


def show_employee_dashboard():

    emp_name = st.session_state.get(
        "emp_name",
        "Employee"
    )

    emp_id = st.session_state.get(
        "emp_id",
        ""
    )

    st.title(
        f"Welcome {emp_name}"
    )

    st.subheader(
        "Upcoming Shifts"
    )

    try:

        response = requests.get(
            f"{API}/api/v1/shifts/{emp_id}"
        )

        if response.status_code == 200:

            data = response.json()

            if len(data) > 0:

                df = pd.DataFrame(data)

                st.dataframe(
                    df,
                    width="stretch"
                )

            else:

                st.info(
                    "No upcoming shifts"
                )

        else:

            st.warning(
                "Unable to fetch shifts"
            )

    except Exception as e:

        st.error(str(e))