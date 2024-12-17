import cv2

from imageBank import ImageBank
from yoloProcessor import YOLOProcessor


class Main:
    def __init__(self):
        self.image_bank = None
        self.yolo_processor = None

    def run(self):
        print("Bienvenue dans le gestionnaire d'images et YOLO.")

        while True:
            print("\n1. Charger un dossier d'images")
            print("2. Afficher la liste des chemins d'images")
            print("3. Afficher chaque image une par une")
            print("4. Traiter les images avec YOLOv8 et enregistrer les résultats")
            print("5. Quitter")

            try:
                choice = int(input("\nEntrez votre choix : "))
            except ValueError:
                print("Veuillez entrer un numéro valide.")
                continue

            if choice == 1:
                self.load_image_folder()
            elif choice == 2:
                self.list_images()
            elif choice == 3:
                self.display_images()
            elif choice == 4:
                self.process_images_with_yolo()
            elif choice == 5:
                print("Au revoir !")
                break
            else:
                print("Choix non valide. Veuillez réessayer.")

    def load_image_folder(self):
        folder_path = input("Entrez le chemin du dossier contenant les images : ").strip()
        try:
            self.image_bank = ImageBank(folder_path)
            print(f"{len(self.image_bank.get_image_paths())} images chargées avec succès.")
            self.yolo_processor = YOLOProcessor(model_path="yolo11x.pt", output_folder="image_traitees")
        except (FileNotFoundError, ValueError) as e:
            print(f"Erreur : {e}")

    def list_images(self):
        if self.image_bank is None:
            print("Veuillez d'abord charger un dossier d'images (option 1).")
            return

        print("\nImages chargées :")
        for image_path in self.image_bank.get_image_paths():
            print(f"- {image_path}")

    def display_images(self):
        if self.image_bank is None:
            print("Veuillez d'abord charger un dossier d'images (option 1).")
            return

        for image_path in self.image_bank:
            try:
                image = cv2.imread(image_path)
                if image is None:
                    print(f"Impossible de charger l'image : {image_path}")
                    continue

                cv2.imshow(f"Image - {image_path}", image)
                print(f"Affichage de l'image : {image_path}")

                key = cv2.waitKey(0)
                if key == 27:
                    print("Affichage interrompu.")
                    break

                cv2.destroyAllWindows()
            except Exception as e:
                print(f"Impossible d'afficher l'image {image_path} : {e}")

        cv2.destroyAllWindows()

    def process_images_with_yolo(self):
        if self.image_bank is None:
            print("Veuillez d'abord charger un dossier d'images (option 1).")
            return

        if self.yolo_processor is None:
            print("Veuillez d'abord initialiser le processeur YOLOv8 (option 1).")
            return

        self.yolo_processor.process_images(self.image_bank.get_image_paths())
        print("Traitement terminé. Images annotées sauvegardées dans le dossier 'image_traitees'.")
