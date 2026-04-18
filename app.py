import streamlit as st
from styles.css import load_css
from components.sidebar import show_sidebar

# إعداد الصفحة
st.set_page_config(page_title="Trading Platform", layout="wide")

# تحميل التصميم
load_css()

# القائمة الجانبية
page = show_sidebar()

# العنوان
st.markdown("<h1 style='text-align:center;'>🚀 منصة التداول</h1>", unsafe_allow_html=True)

# ================= Dashboard =================
if page == "Dashboard":

    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Balance", "$10,000", "+2.5%")
    col2.metric("📈 Profit", "$1,250", "+5.2%")
    col3.metric("📉 Loss", "-$320", "-1.2%")

    st.markdown("---")

    st.markdown("### 📊 Market Overview")
    st.info("Chart will be here")

    st.markdown("### 📡 Signals")
    st.success("BUY EURUSD")
    st.error("SELL BTCUSD")

# ================= Analysis =================
elif page == "تحليل سهم":
    st.markdown("### 📈 تحليل سهم")
    st.info("هنا بيكون تحليل الأسهم")

# ================= Radar =================
elif page == "Radar":
    st.markdown("### 📡 Radar")
    st.info("هنا بيكون الرادار")
