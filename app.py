import streamlit as st
import pandas as pd
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError
import engine as E

# إعداد الصفحة
st.set_page_config(
    page_title="منصة التداول الاحترافية",
    page_icon="💹",
    layout="wide",
)

# حالة الجلسة
if "radar_df" not in st.session_state:
    st.session_state.radar_df = None

# CSS
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #060709;
    color: white;
}
.card {
    background: #0B0D14;
    border: 1px solid #1E2535;
    border-radius: 12px;
    padding: 15px;
}
</style>
""", unsafe_allow_html=True)

# كروت
c1, c2, c3 = st.columns(3)

c1.markdown('<div class="card">BALANCE<br><b>$0</b></div>', unsafe_allow_html=True)
c2.markdown('<div class="card">PROFIT<br><b style="color:#00ff88;">$0</b></div>', unsafe_allow_html=True)
c3.markdown('<div class="card">LOSS<br><b style="color:#ff3366;">$0</b></div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    if st.button("بدء المسح الذكي"):
        
        pairs = ["EURUSD", "GBPUSD", "BTCUSD"]

        results = []

        def scan_one(pair):
            return E.scan(pair)  # لازم تكون موجودة في engine

        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {executor.submit(scan_one, p): p for p in pairs}

            for fut in as_completed(futures):
                pair = futures[fut]
                try:
                    res = fut.result(timeout=10)
                    results.append(res)
                except TimeoutError:
                    results.append({"pair": pair, "signal": "TIMEOUT"})

        df = pd.DataFrame(results)
        st.session_state.radar_df = df

# عرض النتائج
st.subheader("📊 Radar")

if st.session_state.radar_df is not None:
    st.dataframe(st.session_state.radar_df, use_container_width=True)
else:
    st.info("ابدأ المسح من اليسار")
