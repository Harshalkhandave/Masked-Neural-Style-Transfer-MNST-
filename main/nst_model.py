import os
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import numpy as np   
import PIL.Image

class StyleTransferService:
    """
    Neural Style Transfer service using Magenta Hub model.
    Loads model once for efficiency.
    """

    def __init__(self, hub_url: str = "https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2"):
        os.environ["TFHUB_MODEL_LOAD_FORMAT"] = "COMPRESSED"
        self.model = hub.load(hub_url)

    # -----------------------------
    # Image Utilities
    # -----------------------------
    @staticmethod
    def load_image(path_or_pil, max_dim: int = 512):
        """
        Load image from file path or PIL.Image.Image object
        Returns: Tensor [1, H, W, 3]
        """
        if isinstance(path_or_pil, str):
            img = tf.io.read_file(path_or_pil)
            img = tf.image.decode_image(img, channels=3)
        elif isinstance(path_or_pil, Image.Image):
            path_or_pil = path_or_pil.convert("RGB")
            img = tf.convert_to_tensor(np.array(path_or_pil))
        else:
            raise ValueError("Input must be a file path or PIL.Image.Image")

        img = tf.image.convert_image_dtype(img, tf.float32)

        shape = tf.cast(tf.shape(img)[:-1], tf.float32)
        long_dim = tf.reduce_max(shape)
        scale = max_dim / long_dim
        new_shape = tf.cast(shape * scale, tf.int32)

        img = tf.image.resize(img, new_shape)
        img = img[tf.newaxis, :]
        return img

    @staticmethod
    def tensor_to_pil(tensor: tf.Tensor) -> Image.Image:
        tensor = tensor*255
        tensor = np.array(tensor, dtype=np.uint8)
        if np.ndim(tensor)>3:
            assert tensor.shape[0] == 1
            tensor = tensor[0]
        return PIL.Image.fromarray(tensor)

    # -----------------------------
    # Main API Method
    # -----------------------------
    def stylize(self, content, style) -> Image.Image:
        """
        content & style can be:
          - file path (str)
          - PIL.Image.Image
        Returns stylized PIL.Image.Image
        """
        content_tensor = self.load_image(content)
        style_tensor = self.load_image(style)
        stylized_tensor = self.model(
            tf.constant(content_tensor),
            tf.constant(style_tensor)
        )[0]

        return self.tensor_to_pil(stylized_tensor)