from ultralytics import YOLO
import os
import cv2

class YOLOProcessor:
    def __init__(self, model_path='yolo11x.pt', output_folder='processed_images'):
        self.model = self.load_model(model_path)
        self.output_folder = output_folder
        os.makedirs(output_folder, exist_ok=True)

    def load_model(self, model_path):
        try:
            print(f"Chargement du modèle YOLOv8 à partir de {model_path}...")
            model = YOLO(model_path)
            return model
        except Exception as e:
            raise RuntimeError(f"Erreur lors du chargement du modèle YOLOv8 : {e}")

    def process_images(self, image_paths):
        for image_path in image_paths:
            try:
                print(f"Traitement de l'image : {image_path}")

                image = cv2.imread(image_path)
                if image is None:
                    print(f"Impossible de charger l'image : {image_path}")
                    continue

                image_resized = cv2.resize(image, (640, 640))

                results = self.model(image_resized)

                if results and hasattr(results[0], 'boxes'):
                    annotated_image = results[0].plot()
                    output_path = os.path.join(self.output_folder, os.path.basename(image_path))
                    cv2.imwrite(output_path, annotated_image)
                    print(f"Image traitée et enregistrée dans : {output_path}")
                else:
                    print(f"Erreur : Aucun résultat de détection pour l'image {image_path}")

            except Exception as e:
                print(f"Erreur lors du traitement de l'image {image_path} : {e}")
            except KeyboardInterrupt:
                print("Traitement interrompu par l'utilisateur.")
                break
