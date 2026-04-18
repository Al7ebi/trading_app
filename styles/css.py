import streamlit as st

def load_css():
    st.markdown("""
        <style>
        /* خلفية عامة */
        body {
            background-color: #0E1117;
            color: white;
        }

        /* العنوان */
        h1 {
            text-align: center;
            color: #00FFAA;
        }

        /* السايدبار */
        section[data-testid="stSidebar"] {
            background-color: #111827;
        }

        /* الأزرار */
        .stButton>button {
            background-color: #00FFAA;
            color: black;
            border-radius: 10px;
        }

        /* النصوص */
        p {
            font-size: 18px;
        }
        </style>
    """, unsafe_allow_html=True)
