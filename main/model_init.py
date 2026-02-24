from .seg_model import U2NetSegmenter
from .nst_model import StyleTransferService

class ModelLoader:
    """
    Singleton-like loader to cache segmentation and style transfer models
    for fast reuse.
    """

    _segmentation_model: U2NetSegmenter = None
    _nst_model: StyleTransferService = None

    @staticmethod
    def get_segmentation_model() -> U2NetSegmenter:
        """
        Load or return cached U2NetP segmentation model.
        """
        if ModelLoader._segmentation_model is None:
            ModelLoader._segmentation_model = U2NetSegmenter()
        return ModelLoader._segmentation_model

    @staticmethod
    def get_nst_model() -> StyleTransferService:
        """
        Load or return cached TensorFlow Hub style transfer model.
        """
        if ModelLoader._nst_model is None:
            ModelLoader._nst_model = StyleTransferService()
        return ModelLoader._nst_model

