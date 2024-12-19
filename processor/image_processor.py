import os
import cv2
from tqdm import tqdm
from processor.processor import Processor


class ImageProcessor(Processor):
    """
    Class to process images with YOLO and save the results.
    """
    def __init__(self, model_path='yolo11x.pt', output_folder='output/processed_images'):
        """
        Constructor.
        :param model_path: Path to the YOLO model.
        :param output_folder: Folder to save processed images.
        """
        super().__init__(model_path, output_folder)

    def process_images(self, image_paths):
        """
        Process the images with YOLO and save the results.
        :param image_paths: List of image paths to process.
        """
        for image_path in tqdm(image_paths, desc="Processing images", unit="image"):
            try:
                image = cv2.imread(image_path)
                if image is None:
                    continue

                image_resized = cv2.resize(image, (640, 640))
                results = self.model(image_resized)

                if results and hasattr(results[0], 'boxes'):
                    annotated_image = results[0].plot()
                    output_path = os.path.join(self.output_folder, os.path.basename(image_path))
                    cv2.imwrite(output_path, annotated_image)

            except Exception as e:
                print(f"\nError while processing image {image_path}: {e}")
            except KeyboardInterrupt:
                print("\nProcessing interrupted by the user.")
                break