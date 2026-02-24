import streamlit as st
import torch
from app.components.image_selector import get_user_image
from main.stylize import run_stylization
from main.memory_utils import cleanup_memory

def render_background_style():
    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🌄 Style the Background")
    st.markdown("""
    This mode keeps the main subject natural
    and applies the artistic style only to the background.
    
    You may upload your own image or use a sample.
    """)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        content = get_user_image("content")

    with col2:
        style = get_user_image("style")

    st.markdown("---")

    if st.button("✨ Generate Background Style", width="stretch"):
        if content and style:
            with torch.no_grad():
                run_stylization(content, style, mode=2)
        else:
            st.warning("Please provide both content and style images.")
    cleanup_memory()