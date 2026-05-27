import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000/api/v1"

def show_shifts():

    st.title("Shift Management")

    st.subheader("Assign Shift")

    employee_id = st.text_input(
        "Employee ID"
    )

    shift_name = st.selectbox(

        "Shift",

        [
            "Morning",
            "Evening",
            "Night"
        ]
    )

    shift_date = st.date_input(
        "Shift Date"
    )

    # AUTO SHIFT TIMES

    if shift_name == "Morning":

        start_time = "06:00:00"
        end_time = "14:00:00"

    elif shift_name == "Evening":

        start_time = "14:00:00"
        end_time = "22:00:00"

    else:

        start_time = "22:00:00"
        end_time = "06:00:00"

    # HOLIDAY

    is_holiday = st.checkbox(
        "Working on Holiday"
    )

    holiday_note = ""

    if is_holiday:

        holiday_note = st.text_area(
            "Holiday Work Note"
        )

    # SAVE BUTTON

    if st.button("Assign Shift"):

        payload = {

            "employee_id": employee_id,
            "shift_name": shift_name,
            "shift_date": str(shift_date),
            "start_time": start_time,
            "end_time": end_time,
            "is_holiday": is_holiday,
            "holiday_note": holiday_note
        }

        try:

            response = requests.post(

                f"{API}/shifts/create",

                json=payload
            )

            if response.status_code == 200:

                st.success(
                    "Shift Assigned Successfully"
                )

            else:

                st.error(
                    response.text
                )

        except Exception as e:

            st.error(str(e))

    st.divider()

    # SHOW SHIFT TABLE

    try:

        response = requests.get(
            f"{API}/shifts"
        )

        data = response.json()

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            width="stretch"
        )

    except Exception as e:

        st.error(str(e))