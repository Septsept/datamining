import cv2
from menu.menu import Menu
from banks.video_bank import VideoBank
from processor.video_processor import VideoProcessor

class MenuVideo(Menu):
    """
    Class to handle video processing menu.
    """
    def __init__(self):
        """
        Constructor.
        """
        super().__init__()

    def run(self):
        """
        Run the video processing menu.
        """
        print("Welcome to the Video Processing App! - By Septsept")

        while True:
            print("\n1. Load a folder of videos")
            print("2. List the video paths")
            print("3. Display each video one by one")
            print("4. Process the videos with YOLO")
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
        Load a folder of videos.
        """
        folder_path = input("Enter the path to the folder containing the videos:").strip()
        try:
            self.bank = VideoBank(folder_path)
            print(f"{len(self.bank.get_video_paths())} videos loaded successfully.")
            self.yolo_processor = VideoProcessor()
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")

    def display_media(self):
        """
        Display each video one by one.
        """
        if self.bank is None:
            print("Please load a folder of videos first (option 1).")
            return

        for video_path in self.bank:
            try:
                cap = cv2.VideoCapture(video_path)
                if not cap.isOpened():
                    print(f"Unable to open the video: {video_path}")
                    continue

                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break

                    cv2.imshow(f"Video - {video_path}", frame)
                    print(f"Displaying video: {video_path}")

                    key = cv2.waitKey(30)
                    if key == 27:
                        print("Display interrupted.")
                        break

                cap.release()
                cv2.destroyAllWindows()
            except Exception as e:
                print(f"Unable to display the video {video_path}: {e}")

        cv2.destroyAllWindows()

    def process_with_yolo(self):
        """
        Process the videos with YOLO.
        """
        if self.bank is None:
            print("Please load a folder of videos first (option 1).")
            return

        if self.yolo_processor is None:
            print("Please initialize the YOLO processor first (option 1).")
            return

        self.yolo_processor.process_videos(self.bank.get_video_paths())
        print("Processing completed. Annotated videos saved in the 'processed_videos' folder.")