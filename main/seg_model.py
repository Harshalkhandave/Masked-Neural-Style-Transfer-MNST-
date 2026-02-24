from rembg import new_session, remove
from PIL import Image

class U2NetSegmenter:
    """
    U2NetP-based segmentation model using rembg.
    """

    def __init__(self):
        # Initialize once, session cached
        self.session = new_session("u2netp")

    def generate_mask(self, input_image: Image.Image) -> Image.Image:
        """
        Generates a mask from a PIL Image.
        Returns a PIL Image with main object in white and background in black.
        """
        # Ensure RGB
        image = input_image.convert("RGB")
        
        # Remove background using rembg
        result = remove(image, session=self.session)
        
        # Extract alpha channel
        mask = result.split()[-1]
        # Binarize: object=255, background=0
        mask = mask.point(lambda x: 255 if x > 128 else 0)
        return mask

    def generate_mask_from_path(self, input_path: str) -> Image.Image:
        """
        Helper function: input from file path
        """
        image = Image.open(input_path)
        return self.generate_mask(image)

