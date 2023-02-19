import numpy as np


class ObjectDetectorModel:
    """Simulate a segmentation model that extract objects inside an image."""

    def predict(self, image_data: np.ndarray) -> np.ndarray:
        """
        Simulate the call to a model prediction by returning a random mask.

        :param image_data: The input image as a numpy array.
        :return: A mask of a random object detected inside the input image.
        """
        result = np.zeros_like(image_data)
        result = self.add_random_square(result)

        return result

    def add_random_square(self, image_data: np.ndarray) -> np.ndarray:
        """
        Add a random square of 1s inside the input array. Simulate the segmentation of an object within an image.

        :param image_data: The image data as a numpy array.
        :return:
        """
        if image_data.ndim == 3:
            image_data = image_data[:, :, 0]

        rows, cols = image_data.shape

        square_size = np.random.randint(1, min(rows, cols) // 2)
        square_x = np.random.randint(0, cols - square_size)
        square_y = np.random.randint(0, rows - square_size)

        image_data[square_y:square_y + square_size, square_x:square_x + square_size] = 1
        return image_data
