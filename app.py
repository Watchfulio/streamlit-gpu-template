import logging

import streamlit as st

from src.constants import CONFIG

# Configure root logger to capture only WARN or higher level logs
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Configure logger to capture DEBUG-level logs
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

st.set_page_config(layout="wide", page_title=CONFIG["page_title"], page_icon=CONFIG["page_icon"])
st.title(f"{CONFIG['page_icon']} {CONFIG['page_title']}")
st.markdown(f"""
            this is a placeholder for the {CONFIG["name"]} demo
            """)
