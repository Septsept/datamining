from menu.menu_image import MenuImage
from menu.menu_video import MenuVideo

class App:
    """
    Main application class to manage image and video processing.
    """
    def __init__(self):
        """
        Constructor.
        """
        self.image_main = MenuImage()
        self.video_main = MenuVideo()

    def run(self):
        """
        Run the main application.
        :return:
        """
        print("Welcome to the Processing App! - By Septsept")

        while True:
            print("\n1. Process Images")
            print("2. Process Videos")
            print("3. Quit")

            try:
                choice = int(input("\nChoice: "))
            except ValueError:
                print("Invalid choice. Please try again.")
                continue

            if choice == 1:
                self.image_main.run()
            elif choice == 2:
                self.video_main.run()
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = App()
    app.run()