import streamlit as st

def show_sidebar():
    st.sidebar.title("📊 Menu (القائمة)")

    page = st.sidebar.radio(
        "Choose page (اختر الصفحة)",
        ["Dashboard", "تحليل سهم", "Radar"]
    )

    return page
