import streamlit as st
from PIL import Image
MAX_SIZE = 1024

def resize_if_needed(image):
    if max(image.size) > MAX_SIZE:
        image.thumbnail((MAX_SIZE, MAX_SIZE))
    return image

content_images = {
    "Sample Content 1": "images/sampleContent/content1.jpg",
    "Sample Content 2": "images/sampleContent/content2.jpg",
    "Sample Content 3": "images/sampleContent/content3.jpg",
}

style_images = {
    "Sample Style 1": "images/sampleStyle/style1.jpg",
    "Sample Style 2": "images/sampleStyle/style2.jpg",
    "Sample Style 3": "images/sampleStyle/style3.jpg",
}


@st.cache_data
def load_image(path):
    return Image.open(path).convert("RGB")


def get_user_image(image_type: str, instance_id: str = ""):

    if image_type.lower() == "content":
        image_dict = content_images
        label = "Content"
    elif image_type.lower() == "style":
        image_dict = style_images
        label = "Style"
    else:
        st.error("Invalid image type. Use 'content' or 'style'.")
        return None

    options = ["Upload your own"] + list(image_dict.keys())

    option = st.selectbox(
        f"{label} Image",
        options,
        key=f"{image_type}_select_{instance_id}"
    )

    if option == "Upload your own":
        uploaded_file = st.file_uploader(
            f"Upload {label} Image",
            type=["jpg", "jpeg", "png"],
            key=f"{image_type}_upload_{instance_id}"
        )

        if uploaded_file:
            with Image.open(uploaded_file) as img:
                image = img.convert("RGB")
            image = resize_if_needed(image)
            st.image(image, caption=f"{label} Preview", width="stretch")
            return image
        return None

    image = load_image(image_dict[option])
    st.image(image, caption=f"{label} Preview", width="stretch")
    return image