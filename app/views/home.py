import streamlit as st

def render_home():
    st.title("🎨 Masked Neural Style Transfer")
    st.markdown("### Turn your photos into artwork — intelligently 🎭")

    st.markdown("---")

    # =============================
    # Explanation Section
    # =============================

    st.markdown("## 👋 Welcome")
    st.markdown("""
    An AI-powered tool that transforms ordinary photos into artistic visuals by blending structure with creative styles.
    """)
    st.markdown("""
    Scroll below to explore the available modes and click **✨ Try** to begin.
    """)

    st.markdown("---")
    with st.expander("🤔 What is Neural Style Transfer?"):
        st.markdown("""
        Imagine you have:

        • 📷 A normal photo  
        • 🎨 A painting style  

        AI keeps the structure of your photo  
        and applies the artistic style to it.

        Your photo becomes artwork 🎨
        """)

    with st.expander("🎭 What is Masking?"):
        st.markdown("""
        Masking tells AI where to apply style.

        • Only subject  
        • Only background  
        • Different styles for both  

        More control. More creativity ✨
        """)
    st.markdown("---")

    # =============================
    # Original Image (Centered)
    # =============================
    st.markdown("## 📷 Original Content")

    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        st.image("images/samples/content.png", width="stretch")
        st.caption("A peaceful dog in a grassy field — ready for an artistic makeover 🎨")
    st.markdown("---")

    
    st.markdown("## 🖼 Example Modes")

    # =============================
    # ROW 1
    # =============================
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎨 Full Image Style")
        st.markdown("""
        Style is applied to the entire image.
        Simple and classic NST.
        """)
        st.image("images/samples/stylized.jpg", width="stretch")
        btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
        with btn_col2:
            if st.button("✨ Try Full Image Style", key="full", width="stretch"):
                st.session_state.page = "Full Style"
                st.rerun()

    with col2:
        st.markdown("### 🎯 Style the Subject")
        st.markdown("""
        Only the main object gets stylized.
        Background remains original.
        """)
        st.image("images/samples/oMasked.jpg", width="stretch")
        btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
        with btn_col2:
            if st.button("✨ Try Subject Style", key="subject", width="stretch"):
                st.session_state.page = "Subject Style"
                st.rerun()

    st.markdown("---")

    # =============================
    # ROW 2
    # =============================
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### 🌄 Style the Background")
        st.markdown("""
        Only background is stylized.
        Subject remains natural.
        """)
        st.image("images/samples/bMasked.jpg", width="stretch")
        btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
        with btn_col2:
            if st.button("✨ Try Background Style", key="background", width="stretch"):
                st.session_state.page = "Background Style"
                st.rerun()

    with col4:
        st.markdown("### 🌈 Dual Style (Advanced)")
        st.markdown("""
        Apply two different styles:
        one for subject and one for background.
        """)
        st.image("images/samples/obMasked.jpg", width="stretch")
        btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
        with btn_col2:
            if st.button("✨ Try Dual Style", key="dual", width="stretch"):
                st.session_state.page = "Dual Style"
                st.rerun()

    st.markdown("---")

    # # =============================
    # # Footer
    # # =============================
    # st.markdown("### 👨‍💻 About the Creator")
    # st.markdown("""
    # Built by **Harshal Khandave**

    # 🚀 Embedded + AI Engineer  
    # 🎯 Passionate about Deep Learning & Computer Vision  
    # 📌 Exploring creative AI systems
    # """)

    st.success("⬅️ Use the sidebar anytime to switch modes.")