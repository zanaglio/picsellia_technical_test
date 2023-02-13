import base64
import io

import numpy as np
from PIL import Image


def base64_to_array(image_base64, data_type=np.uint8):
    """
    Decode a base64 encoded image into a numpy array.
    """

    image_bytes = io.BytesIO(base64.b64decode(image_base64))
    image = Image.open(image_bytes)
    image_data = np.array(image, dtype=data_type)
    image.close()

    return image_data


def array_to_base64(image_data):
    """
    Convert a numpy array to base64.
    """

    buffered = io.BytesIO()

    image = Image.fromarray(image_data.astype(np.uint8))

    image.save(buffered, format="png")
    image_base64 = base64.b64encode(buffered.getvalue())
    image.close()

    return str(image_base64.decode('utf8'))


def bytes_to_base64(image_bytes: bytes) -> str:
    """
    Convert bytes to base64
    """
    
    return base64.b64encode(image_bytes).decode()
