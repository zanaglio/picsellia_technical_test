import numpy as np
from imantics import Mask


def extract_vertices(image_data: np.ndarray) -> list:
    """
    Get the vertices (list of tuple (x, y)) of all the polygons inside an image. The function only support images
    composed by either 0s and 1s.

    :param image_data: The image to extract the object's vertices.
    :return: A list of vertices. A vertex is a list containing tuples of (x, y) coordinates.
    """
    if image_data.size == 0:
        raise ValueError("Cannot handle multiclass when extracting vertices.")

    elif image_data.ndim != 2:
        raise ValueError(f"Cannot compute the outlines' vertices with a {image_data.ndim}-channels image.")

    elif image_data.min() != 0 or image_data.max() != 1:
        raise ValueError("Cannot handle multiclass images when extracting vertices. Check the prediction output.")

    return [[(int(point[0]), int(point[1])) for point in polygon] for polygon in Mask(image_data).polygons().points]
