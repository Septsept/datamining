import os

class ImageBank:
    """
    Class to manage a folder of images.
    """
    def __init__(self, folder_path):
        """
        Constructor.
        :param folder_path:
        """
        self.folder_path = folder_path
        self.image_paths = []
        self._current_index = 0
        self.load_images()

    def load_images(self):
        """
        Load the images from the folder.
        :return:
        """
        if not os.path.exists(self.folder_path):
            raise FileNotFoundError(f"Folder not found: {self.folder_path}")

        supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
        self.image_paths = [
            os.path.join(self.folder_path, f)
            for f in os.listdir(self.folder_path)
            if f.lower().endswith(supported_formats)
        ]

        if not self.image_paths:
            raise ValueError("No valid image found in the folder.")

    def __iter__(self):
        """
        Iterator method.
        :return:
        """
        self._current_index = 0
        return self

    def __next__(self):
        """
        Next method.
        :return:
        """
        if self._current_index >= len(self.image_paths):
            raise StopIteration

        image_path = self.image_paths[self._current_index]
        self._current_index += 1
        return image_path

    def get_image_paths(self):
        """
        Get the list of image paths.
        :return:
        """
        return self.image_paths