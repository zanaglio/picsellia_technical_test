import numpy as np


def predict(image_data: np.array) -> np.array:
    """
    Simulate the call to a model prediction by returning a random mask.

    :param image_data: The input image as a numpy array.
    :return: A mask of a random object detected inside the input image.
    """
    image_width = image_data.width
    image_height = image_data.height

    result = np.zeros((image_width, image_height), dtype=int)
    result = add_random_square(result)

    return result


def add_random_square(image_data: np.array) -> np.array:
    """
    Add a random square of 1s inside the input array. Simulate the segmentation of an object within an image.

    :param image_data: The image data as a numpy array.
    :return:
    """
    rows, cols = image_data.shape

    square_size = np.random.randint(1, min(rows, cols) // 2)
    square_x = np.random.randint(0, cols - square_size)
    square_y = np.random.randint(0, rows - square_size)

    image_data[square_y:square_y + square_size, square_x:square_x + square_size] = 1
    return image_data
