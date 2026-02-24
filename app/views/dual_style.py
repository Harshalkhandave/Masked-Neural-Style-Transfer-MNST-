import streamlit as st
from app.components.image_selector import get_user_image
from main.stylize import run_stylization
from main.memory_utils import cleanup_memory
import torch

def render_dual_style():
    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🌈 Dual Style (Subject + Background)")
    st.markdown("""
    This advanced mode lets you apply:
    
    • One artistic style to the subject  
    • A different style to the background  
    
    Perfect for maximum creative control.
    
    You can upload your own images or select samples.
    """)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        content = get_user_image("content")

    with col2:
        style_1 = get_user_image("style",1)

    with col3:
        style_2 = get_user_image("style",2)

    st.markdown("---")

    if st.button("✨ Generate Dual Style", width="stretch"):
        if content and style_1 and style_2:
            with torch.no_grad():
                run_stylization(content, style_1, mode=3, secondary_style=style_2)
        else:
            st.warning("Please provide all required images.")
    cleanup_memory()