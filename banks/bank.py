import os

class Bank:
    """
    Base class to manage a folder of media files.
    """
    def __init__(self, folder_path, supported_formats):
        """
        Constructor.
        :param folder_path: Path to the folder containing media files.
        :param supported_formats: Tuple of supported file formats.
        """
        self.folder_path = folder_path
        self.media_paths = []
        self._current_index = 0
        self.supported_formats = supported_formats
        self.load_media()

    def load_media(self):
        """
        Load the media files from the folder.
        :return:
        """
        if not os.path.exists(self.folder_path):
            raise FileNotFoundError(f"Folder not found: {self.folder_path}")

        self.media_paths = [
            os.path.join(self.folder_path, f)
            for f in os.listdir(self.folder_path)
            if f.lower().endswith(self.supported_formats)
        ]

        if not self.media_paths:
            raise ValueError("No valid media files found in the folder.")

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
        if self._current_index >= len(self.media_paths):
            raise StopIteration

        media_path = self.media_paths[self._current_index]
        self._current_index += 1
        return media_path

    def get_paths(self):
        """
        Get the list of media paths.
        :return:
        """
        return self.media_paths