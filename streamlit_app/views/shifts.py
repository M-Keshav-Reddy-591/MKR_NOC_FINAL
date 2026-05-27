import streamlit as st


def show_shifts():

    st.title("SHIFT MANAGEMENT")

    st.selectbox(

        "Select Shift",

        [
            "Morning",
            "Evening",
            "Night",
            "Holiday"
        ]
    )

    st.button("Assign Shift")