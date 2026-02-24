import streamlit as st
from PIL import Image
import torchvision
from main.model_init import ModelLoader
from main.utils import load_image_tensor, apply_mask_blend
import gc
import torch

# =====================================================
# Load Models (Cached)
# =====================================================
@st.cache_resource
def load_models():
    segmentation_model = ModelLoader.get_segmentation_model()
    style_transfer_model = ModelLoader.get_nst_model()
    return segmentation_model, style_transfer_model


segmentation_model, style_transfer_model = load_models()


# =====================================================
# Stylization Pipeline
# =====================================================
def run_stylization(content_input, style_input, mode=0, secondary_style=None):
    """
    mode:
        0 -> Full Image Style
        1 -> Subject Style
        2 -> Background Style
        3 -> Dual Style
    """
    content_image = Image.open(content_input) if isinstance(content_input, str) else content_input
    style_image = Image.open(style_input) if isinstance(style_input, str) else style_input

    with st.spinner("Applying Neural Style Transfer..."):
        stylized_image = style_transfer_model.stylize(content_image, style_image)

    content_image = content_image.resize(stylized_image.size)

    if mode == 0:
        stylized_image.save("output_masked.jpg")
    else :
        mask = segmentation_model.generate_mask(content_image)

        content_tensor = load_image_tensor(content_image)
        stylized_tensor = load_image_tensor(stylized_image)

        if mode == 1:  # Subject Style
            final_tensor = apply_mask_blend(content_tensor, stylized_tensor, mask)

        elif mode == 2:  # Background Style
            final_tensor = apply_mask_blend(stylized_tensor, content_tensor, mask)

        elif mode == 3 and secondary_style:  # Dual Style
            secondary_style_image = Image.open(secondary_style) if isinstance(secondary_style, str) else secondary_style
            stylized_image_2 = style_transfer_model.stylize(content_image, secondary_style_image)
            stylized_image_2 = stylized_image_2.resize(stylized_image.size)
            stylized_tensor_2 = load_image_tensor(stylized_image_2)

            final_tensor = apply_mask_blend(stylized_tensor_2, stylized_tensor, mask)

        torchvision.utils.save_image(final_tensor, "output_masked.jpg")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.success("Stylization Complete ✅")
        st.image("output_masked.jpg", caption="Masked Stylized Image", width="stretch")

        with open("output_masked.jpg", "rb") as f:
            st.download_button(
                label="⬇️ Download Stylized Image",
                data=f,
                file_name="stylized_image.jpg",
                mime="image/jpeg",
                width="stretch"
            )
    # 🔥 MEMORY CLEANUP SECTION
    del content_image, style_image, stylized_image

    gc.collect()

    if torch.cuda.is_available():
        torch.cuda.empty_cache()
