import os
from ultralytics import YOLO

class Processor:
    """
    Base class for processing media with YOLO.
    """
    def __init__(self, model_path, output_folder):
        """
        Constructor.
        :param model_path: Path to the YOLO model.
        :param output_folder: Folder to save processed media.
        """
        self.model = self.load_model(model_path)
        self.output_folder = output_folder
        self.create_output_folders()

    def load_model(self, model_path):
        """
        Load the YOLO model from the specified path.
        :param model_path: Path to the YOLO model.
        :return: Loaded YOLO model.
        """
        try:
            print(f"Loading YOLO model from {model_path}...")
            model = YOLO(model_path)
            return model
        except Exception as e:
            raise RuntimeError(f"Error loading YOLO model: {e}")

    def create_output_folders(self):
        """
        Create the output folders if they do not exist.
        """
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

