import streamlit as st
from styles.css import load_css
from components.sidebar import show_sidebar

# إعداد الصفحة
st.set_page_config(page_title="Trading Platform", layout="wide")

# تحميل CSS
load_css()

# 🌙 وضع ليلي / نهاري
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

col1, col2 = st.columns([10,1])

with col2:
    if st.session_state.theme == "dark":
        if st.button("☀️"):
            st.session_state.theme = "light"
    else:
        if st.button("🌙"):
            st.session_state.theme = "dark"

# تطبيق الثيم
if st.session_state.theme == "dark":
    st.markdown("""
        <style>
        body { background-color: #0e1117; color: white; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body { background-color: white; color: black; }
        </style>
    """, unsafe_allow_html=True)

# القائمة الجانبية
page = show_sidebar()

# العنوان الرئيسي
st.markdown("<h1 style='text-align:center;'>🚀 منصة التداول</h1>", unsafe_allow_html=True)

# الصفحات
if page == "Dashboard":
    st.markdown("### 📊 الصفحة الرئيسية")
    st.write("Welcome to your trading dashboard")

elif page == "تحليل سهم":
    st.markdown("### 📈 تحليل سهم")
    st.write("Stock analysis tools will be here")

elif page == "Radar":
    st.markdown("### 📡 Radar")
    st.write("Market scanner (coming soon)")
