import streamlit as st
from app.components.image_selector import get_user_image
from main.stylize import run_stylization
import torch
from main.memory_utils import cleanup_memory

def render_subject_style():
    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🎯 Style the Subject")
    st.markdown("""
    This mode detects the main subject (like a person or object) 
    and applies the artistic style only to that part.
    
    Background remains unchanged.
    
    You can upload your own images or choose from samples.
    """)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        content = get_user_image("content")

    with col2:
        style = get_user_image("style")

    st.markdown("---")

    if st.button("✨ Generate Subject Style", width="stretch"):
        if content and style:
            with torch.no_grad():
                run_stylization(content, style, mode=1)
        else:
            st.warning("Please provide both content and style images.")
    cleanup_memory()