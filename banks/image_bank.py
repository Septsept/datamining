from banks.bank import Bank

class ImageBank(Bank):
    """
    Class to manage a folder of images.
    """
    def __init__(self, folder_path):
        """
        Constructor.
        :param folder_path: Path to the folder containing images.
        """
        supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
        super().__init__(folder_path, supported_formats)

    def get_image_paths(self):
        """
        Get the list of image paths.
        :return: List of image paths.
        """
        return self.get_paths()