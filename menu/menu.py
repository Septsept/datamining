class Menu:
    """
    Base class for menu handling.
    """
    def __init__(self):
        """
        Constructor.
        """
        self.bank = None
        self.yolo_processor = None

    def run(self):
        """
        Run the menu.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def load_folder(self):
        """
        Load a folder of media.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def list_media(self):
        """
        List the media paths.
        """
        if self.bank is None:
            print("Please load a folder first (option 1).")
            return

        print("\nMedia loaded:")
        for media_path in self.bank.get_paths():
            print(f"- {media_path}")

    def display_media(self):
        """
        Display each media one by one.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def process_with_yolo(self):
        """
        Process the media with YOLO.
        """
        raise NotImplementedError("Subclasses should implement this method.")