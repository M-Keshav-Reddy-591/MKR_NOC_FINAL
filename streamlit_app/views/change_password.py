# import streamlit as st
# import requests

# API = "http://127.0.0.1:8000/api/v1"

# def show_change_password():

#     st.title("Change Password")

#     employee_id = st.text_input(
#         "Employee ID"
#     )

#     old_password = st.text_input(
#         "Old Password",
#         type="password"
#     )

#     new_password = st.text_input(
#         "New Password",
#         type="password"
#     )

#     if st.button("Change Password"):

#         payload = {

#             "employee_id": employee_id,
#             "old_password": old_password,
#             "new_password": new_password
#         }

#         try:

#             response = requests.post(

#                 f"{API}/auth/change-password",

#                 json=payload
#             )

#             if response.status_code == 200:

#                 st.success(
#                     "Password Updated Successfully"
#                 )

#             else:

#                 st.error(
#                     response.json()["detail"]
#                 )

#         except Exception as e:

#             st.error(str(e))




import streamlit as st
import requests

API = "http://127.0.0.1:8000"


def show_change_password():

    st.title("Change Password")

    employee_id = st.text_input(
        "Employee ID",
        value=st.session_state.emp_id
    )

    old_password = st.text_input(
        "Old Password",
        type="password"
    )

    new_password = st.text_input(
        "New Password",
        type="password"
    )

    if st.button(
        "Change Password",
        width="stretch"
    ):

        response = requests.post(

            f"{API}/api/v1/auth/change-password",

            json={

                "employee_id": employee_id,

                "old_password": old_password,

                "new_password": new_password

            }

        )

        try:

            data = response.json()

        except:

            st.error(
                "Backend response error"
            )

            return

        if response.status_code == 200:

            st.success(
                data["message"]
            )

        else:

            st.error(
                data["detail"]
            )