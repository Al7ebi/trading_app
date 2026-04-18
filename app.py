import streamlit as st
from styles.css import load_css
from components.sidebar import show_sidebar

# صفحات
from pages.dashboard import show_dashboard
from pages.single import show_single
from pages.radar import show_radar

# إعداد الصفحة
st.set_page_config(page_title="Trading Platform", layout="wide")

# تحميل CSS
load_css()

# القائمة
page = show_sidebar()

# التنقل
if page == "Dashboard":
    show_dashboard()

elif page == "تحليل سهم":
    show_single()

elif page == "Radar":
    show_radar()
