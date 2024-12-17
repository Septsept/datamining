from ultralytics import YOLO
import os
import cv2

class YOLOProcessor:
    """
    Class to process images with YOLO and save the results.
    """
    def __init__(self, model_path='yolo11x.pt', output_folder='processed_images'):
        """
        Constructor.
        :param model_path:
        :param output_folder:
        """
        self.model = self.load_model(model_path)
        self.output_folder = output_folder
        os.makedirs(output_folder, exist_ok=True)

    def load_model(self, model_path):
        """
        Load the YOLO model from the specified path.
        :param model_path:
        :return:
        """
        try:
            print(f"Loading YOLO model from {model_path}...")
            model = YOLO(model_path)
            return model
        except Exception as e:
            raise RuntimeError(f"Error loading YOLO model: {e}")

    def process_images(self, image_paths):
        """
        Process the images with YOLO and save the results.
        :param image_paths:
        :return:
        """
        for image_path in image_paths:
            try:
                print(f"Processing image: {image_path}")

                image = cv2.imread(image_path)
                if image is None:
                    print(f"Unable to load the image: {image_path}")
                    continue

                image_resized = cv2.resize(image, (640, 640))

                results = self.model(image_resized)

                if results and hasattr(results[0], 'boxes'):
                    annotated_image = results[0].plot()
                    output_path = os.path.join(self.output_folder, os.path.basename(image_path))
                    cv2.imwrite(output_path, annotated_image)
                    print(f"Image processed and saved in: {output_path}")
                else:
                    print(f"Error: No detection result for image {image_path}")

            except Exception as e:
                print(f"Error while processing image {image_path}: {e}")
            except KeyboardInterrupt:
                print("Processing interrupted by the user.")
                break
