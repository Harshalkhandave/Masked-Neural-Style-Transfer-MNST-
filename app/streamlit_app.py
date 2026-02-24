import streamlit as st
from app.views import PAGES


# =====================================================
# Page Configuration
# =====================================================
st.set_page_config(
    page_title="Masked Neural Style Transfer",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# Get Page Names (Single Source of Truth)
# =====================================================
page_names = list(PAGES.keys())


# =====================================================
# Sidebar Navigation
# =====================================================
with st.sidebar:
    st.markdown("## 🎨 Masked Neural Style Transfer")
    st.markdown("---")

    # Initialize session state safely
    if "page" not in st.session_state or st.session_state.page not in page_names:
        st.session_state.page = page_names[0]

    selected_page = st.radio(
        "Choose Mode",
        page_names,
        index=page_names.index(st.session_state.page),
        label_visibility="collapsed"
    )

    st.session_state.page = selected_page

    st.markdown("---")
    st.info("Select a mode and upload images to begin.")


# =====================================================
# Page Routing
# =====================================================
PAGES[st.session_state.page]()


# =====================================================
# Footer
# =====================================================
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & PyTorch")