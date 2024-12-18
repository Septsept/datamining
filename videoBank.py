import os

class VideoBank:
    """
    Class to manage a folder of videos.
    """
    def __init__(self, folder_path):
        """
        Constructor.
        :param folder_path:
        """
        self.folder_path = folder_path
        self.video_paths = []
        self._current_index = 0
        self.load_videos()

    def load_videos(self):
        """
        Load the videos from the folder.
        :return:
        """
        if not os.path.exists(self.folder_path):
            raise FileNotFoundError(f"Folder not found: {self.folder_path}")

        supported_formats = ('.mp4', '.avi', '.mov', '.mkv')
        self.video_paths = [
            os.path.join(self.folder_path, f)
            for f in os.listdir(self.folder_path)
            if f.lower().endswith(supported_formats)
        ]

        if not self.video_paths:
            raise ValueError("No valid video found in the folder.")

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
        if self._current_index >= len(self.video_paths):
            raise StopIteration

        video_path = self.video_paths[self._current_index]
        self._current_index += 1
        return video_path

    def get_video_paths(self):
        """
        Get the list of video paths.
        :return:
        """
        return self.video_paths