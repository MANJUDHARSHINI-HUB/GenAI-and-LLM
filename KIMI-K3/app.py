import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Ryomen Sukuna - 3D Showcase",
    page_icon="⛩️",
    layout="wide"
)

# Remove default Streamlit padding so the showcase fills the page cleanly
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

html_file = Path(__file__).parent / "index.html"
html_code = html_file.read_text(encoding="utf-8")

components.html(
    html_code,
    height=1100,
    scrolling=True
)
