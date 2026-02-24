import streamlit as st
from app.components.image_selector import get_user_image
from main.stylize import run_stylization
import torch
from main.memory_utils import cleanup_memory

def render_full_image_style():
    # Back button
    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🎨 Full Image Style")
    st.markdown("""
    This mode applies the selected artistic style to the **entire image**.
    
    You can upload your own images or choose from samples.
    Both content and style are required.
    """)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        content = get_user_image("content")

    with col2:
        style = get_user_image("style")

    st.markdown("---")

    if st.button("✨ Generate Full Image Style", width="stretch"):
        if content and style:
            with torch.no_grad():
                run_stylization(content, style, mode=0)
        else:
            st.warning("Please provide both content and style images.")           
    cleanup_memory()