import streamlit as st
from styles.css import load_css
from components.sidebar import show_sidebar

# تحميل الستايل
load_css()

# القائمة الجانبية
page = show_sidebar()

# عنوان التطبيق
st.title("منصة التداول 🚀")

# التنقل بين الصفحات
if page == "Dashboard":
    st.write("Main page (الصفحة الرئيسية)")

elif page == "تحليل سهم":
    st.write("Stock analysis (تحليل سهم)")

elif page == "Radar":
    st.write("Radar page (صفحة الرادار)")
