import torch
import torchvision
from torchvision import transforms
import torch.nn.functional as F
from main.model_init import ModelLoader
import numpy as np
from PIL import Image
import streamlit as st
# =====================================================
# Device Setup
# =====================================================
is_cuda_available = torch.cuda.is_available()
tensor_dtype = torch.cuda.FloatTensor if is_cuda_available else torch.FloatTensor

image_transform = transforms.Compose([transforms.ToTensor()])

# =====================================================
# Utility Functions
# =====================================================
def load_image_tensor(image: Image.Image):
    """Convert PIL image to torch tensor"""
    tensor = image_transform(image).unsqueeze(0)
    return tensor.type(tensor_dtype)


def apply_mask_blend(content_tensor, stylized_tensor, mask_image):
    """Blend stylized and content image using segmentation mask"""
    mask_np = np.array(mask_image) / 255.0
    mask_tensor = torch.from_numpy(mask_np).unsqueeze(0).unsqueeze(0).float()
    mask_tensor = mask_tensor.to(stylized_tensor.device)

    mask_tensor = F.interpolate(
        mask_tensor,
        size=stylized_tensor.shape[2:],
        mode="nearest"
    )

    return stylized_tensor * mask_tensor + content_tensor * (1 - mask_tensor)
