import cv2
from menu.menu import Menu
from banks.image_bank import ImageBank
from processor.image_processor import ImageProcessor

class MenuImage(Menu):
    """
    Class to handle image processing menu.
    """
    def __init__(self):
        """
        Constructor.
        """
        super().__init__()

    def run(self):
        """
        Run the image processing menu.
        """
        print("Welcome to the Image Processing App! - By Septsept")

        while True:
            print("\n1. Load a folder of images")
            print("2. List the image paths")
            print("3. Display each image one by one")
            print("4. Process the images with YOLO")
            print("5. Back to media type selection")

            try:
                choice = int(input("\nChoice: "))
            except ValueError:
                print("Invalid choice. Please try again.")
                continue

            if choice == 1:
                self.load_folder()
            elif choice == 2:
                self.list_media()
            elif choice == 3:
                self.display_media()
            elif choice == 4:
                self.process_with_yolo()
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def load_folder(self):
        """
        Load a folder of images.
        """
        folder_path = input("Enter the path to the folder containing the images:").strip()
        try:
            self.bank = ImageBank(folder_path)
            print(f"{len(self.bank.get_image_paths())} images loaded successfully.")
            self.yolo_processor = ImageProcessor(model_path="yolo11x.pt", output_folder="output/processed_images")
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")

    def display_media(self):
        """
        Display each image one by one.
        """
        if self.bank is None:
            print("Please load a folder of images first (option 1).")
            return

        for image_path in self.bank:
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

    def process_with_yolo(self):
        """
        Process the images with YOLO.
        """
        if self.bank is None:
            print("Please load a folder of images first (option 1).")
            return

        if self.yolo_processor is None:
            print("Please initialize the YOLO processor first (option 1).")
            return

        self.yolo_processor.process_images(self.bank.get_image_paths())
        print("Processing completed. Annotated images saved in the 'processed_images' folder.")