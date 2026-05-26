import streamlit as st

st.title("SHIFT MANAGEMENT")

employee = st.text_input(
    "Employee ID"
)

shift = st.selectbox(
    "Shift",
    [
        "Morning",
        "Evening",
        "Night",
        "Holiday"
    ]
)

date = st.date_input(
    "Shift Date"
)

notes = st.text_area(
    "Holiday Notes"
)

if st.button("Assign Shift"):

    st.success(
        "Shift Assigned Successfully"
    )