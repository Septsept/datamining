import os

class ImageBank:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.image_paths = []
        self._current_index = 0
        self.load_images()

    def load_images(self):
        if not os.path.exists(self.folder_path):
            raise FileNotFoundError(f"Dossier non trouvé : {self.folder_path}")

        supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
        self.image_paths = [
            os.path.join(self.folder_path, f)
            for f in os.listdir(self.folder_path)
            if f.lower().endswith(supported_formats)
        ]

        if not self.image_paths:
            raise ValueError("Aucune image valide trouvée dans le dossier.")

    def __iter__(self):
        self._current_index = 0
        return self

    def __next__(self):
        if self._current_index >= len(self.image_paths):
            raise StopIteration

        image_path = self.image_paths[self._current_index]
        self._current_index += 1
        return image_path

    def get_image_paths(self):
        return self.image_paths