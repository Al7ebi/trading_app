
import streamlit as st

def show_sidebar():
    st.sidebar.title("📊 Menu")

    page = st.sidebar.radio(
        "Choose page",
        ["Dashboard", "تحليل سهم", "Radar"]
    )

    return page
