import streamlit as st
from styles.css import load_css
from components.sidebar import show_sidebar

# اختيار الوضع
mode = st.sidebar.radio("🌙 / ☀️", ["Dark", "Light"])

# تطبيق الثيم
def apply_theme(mode):
    if mode == "Dark":
        st.markdown("""
        <style>
        body { background-color: #0E1117; color: white; }
        h1 { color: #00FFAA; text-align: center; }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        body { background-color: white; color: black; }
        h1 { color: #333; text-align: center; }
        </style>
        """, unsafe_allow_html=True)

apply_theme(mode)

# القائمة الجانبية
page = show_sidebar()

# العنوان
st.title("منصة التداول 🚀")

# الصفحات
if page == "Dashboard":
    st.write("Main page (الصفحة الرئيسية)")

elif page == "تحليل سهم":
    st.write("Stock analysis (تحليل سهم)")

elif page == "Radar":
    st.write("Radar page (صفحة الرادار)")
