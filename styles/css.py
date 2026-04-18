def load_css():
    import streamlit as st

    st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
