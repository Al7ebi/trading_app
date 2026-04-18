import streamlit as st
from styles.css import load_css
from components.sidebar import show_sidebar

load_css()

page = show_sidebar()

st.title("منصة التداول 🚀")

if page == "Dashboard":
    st.write("Main page (الصفحة الرئيسية)")

elif page == "تحليل سهم":
    st.write("Stock analysis (تحليل سهم)")

elif page == "Radar":
    st.write("Radar page (صفحة الرادار)")
