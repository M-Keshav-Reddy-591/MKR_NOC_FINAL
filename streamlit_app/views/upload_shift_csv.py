import streamlit as st
import pandas as pd
import requests

API = "http://127.0.0.1:8000"


def show_upload_shift_csv():

    st.title("CSV Shift Upload")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(
                uploaded_file,
                index_col=False,
                encoding="utf-8"
            )

        st.subheader("Preview")

        st.dataframe(
            df,
            width="stretch"
        )

        if st.button(
            "Upload Shifts",
            width="stretch"
        ):
                        
            success = 0
            failed = 0

            for _, row in df.iterrows():

                payload = {

                    "employee_id": str(
                        row["employee_id"]
                    ),

                    "shift_name": str(
                        row["shift_name"]
                    ),

                    "shift_date": str(
                        row["shift_date"]
                    ),

                    "start_time": str(
                        row["start_time"]
                    ),

                    "end_time": str(
                        row["end_time"]
                    ),

                    "is_holiday": bool(
                        row["holiday"]
                    ),

                    "holiday_note": str(
                        row["holiday_note"]
                    )

                }

                response = requests.post(

                    f"{API}/api/v1/shifts/create",

                    json=payload

                )

                if response.status_code == 200:

                    success += 1

                else:

                    failed += 1

                    try:

                        st.error(
                            response.json()["detail"]
                        )

                    except:

                        st.error(
                            response.text
                        )

            st.success(
                f"{success} shifts uploaded"
            )

            if failed > 0:

                st.error(
                    f"{failed} uploads failed"
                )



            # success = 0
            # failed = 0


            # for _, row in df.iterrows():

            #     payload = {

            #         "employee_id": str(
            #             row["employee_id"]
            #         ),

            #         "shift_name": str(
            #             row["shift_name"]
            #         ),

            #         "shift_date": str(
            #             row["shift_date"]
            #         ),

            #         "start_time": str(
            #             row["start_time"]
            #         ),

            #         "end_time": str(
            #             row["end_time"]
            #         ),

            #         "is_holiday": bool(
            #             row["holiday"]
            #         )

            #     }

            #     # requests.post(
            #     #     f"{API}/api/v1/shifts/create",
            #     #     json=payload
            #     # )

            # # for _, row in df.iterrows():

            # #     payload = {

            # #         "employee_id":
            # #         row["employee_id"],

            # #         "shift_name":
            # #         row["shift_name"],

            # #         "shift_date":
            # #         str(row["shift_date"]),

            # #         "start_time":
            # #         str(row["start_time"]),

            # #         "end_time":
            # #         str(row["end_time"])

            # #     }

            #     response = requests.post(

            #         f"{API}/api/v1/shifts/create",

            #         json=payload

            #     )

            #     if response.status_code == 200:

            #         success += 1

            #     else:

            #         failed += 1

            # st.success(
            #     f"{success} shifts uploaded"
            # )

            # if failed > 0:

            #     st.error(
            #         f"{failed} uploads failed"
            #     )

