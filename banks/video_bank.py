from banks.bank import Bank

class VideoBank(Bank):
    """
    Class to manage a folder of videos.
    """
    def __init__(self, folder_path):
        """
        Constructor.
        :param folder_path: Path to the folder containing videos.
        """
        supported_formats = ('.mp4', '.avi', '.mov', '.mkv')
        super().__init__(folder_path, supported_formats)

    def get_video_paths(self):
        """
        Get the list of video paths.
        :return: List of video paths.
        """
        return self.get_paths()