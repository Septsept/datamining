import cv2

from imageBank import ImageBank
from yoloProcessor import YOLOProcessor


class Main:
    """
    Main class to manage images and YOLO processing.
    """
    def __init__(self):
        """
        Constructor.
        """
        self.image_bank = None
        self.yolo_processor = None

    def run(self):
        """
        Run the main application.
        :return:
        """
        print("Welcome to the Image Processing App ! - By Septsept")

        while True:
            print("\n1. Load a folder of images")
            print("2. List the image paths")
            print("3. Display each image one by one")
            print("4. Process the images with YOLO")
            print("5. Quit")

            try:
                choice = int(input("\nChoice: "))
            except ValueError:
                print("Invalid choice. Please try again.")
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
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def load_image_folder(self):
        """
        Load a folder of images.
        :return:
        """
        folder_path = input("Enter the path to the folder containing the images:").strip()
        try:
            self.image_bank = ImageBank(folder_path)
            print(f"{len(self.image_bank.get_image_paths())} images loaded successfully.")
            self.yolo_processor = YOLOProcessor(model_path="yolo11x.pt", output_folder="processed_images")
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")

    def list_images(self):
        """
        List the image paths.
        :return:
        """
        if self.image_bank is None:
            print("Please load a folder of images first (option 1).")
            return

        print("\nImages loaded:")
        for image_path in self.image_bank.get_image_paths():
            print(f"- {image_path}")

    def display_images(self):
        """
        Display each image one by one.
        :return:
        """
        if self.image_bank is None:
            print("Please load a folder of images first (option 1).")
            return

        for image_path in self.image_bank:
            try:
                image = cv2.imread(image_path)
                if image is None:
                    print(f"Unable to load the image: {image_path}")
                    continue

                cv2.imshow(f"Image - {image_path}", image)
                print(f"Displaying image: {image_path}")

                key = cv2.waitKey(0)
                if key == 27:
                    print("Display interrupted.")
                    break

                cv2.destroyAllWindows()
            except Exception as e:
                print(f"Unable to display the image {image_path}: {e}")

        cv2.destroyAllWindows()

    def process_images_with_yolo(self):
        """
        Process the images with YOLO.
        :return:
        """
        if self.image_bank is None:
            print("Please load a folder of images first (option 1).")
            return

        if self.yolo_processor is None:
            print("Please initialize the YOLO processor first (option 1).")
            return

        self.yolo_processor.process_images(self.image_bank.get_image_paths())
        print("Processing completed. Annotated images saved in the 'processed_images' folder.")
