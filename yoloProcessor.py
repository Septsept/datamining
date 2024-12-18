import cv2
import os
from tqdm import tqdm

class YOLOProcessor:
    """
    Class to process videos using YOLO.
    """
    def __init__(self, model_path, output_folder):
        """
        Constructor.
        :param model_path:
        :param output_folder:
        """
        self.model = self.load_model(model_path)
        self.output_folder = output_folder
        self.create_output_folder()

    def load_model(self, model_path):
        """
        Load the YOLO model.
        :param model_path:
        :return:
        """
        from ultralytics import YOLO
        return YOLO(model_path)

    def create_output_folder(self):
        """
        Create the output folder if it does not exist.
        :return:
        """
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def process_videos(self, video_paths):
        """
        Process the videos using YOLO.
        :param video_paths:
        :return:
        """
        for video_path in video_paths:
            try:
                print(f"Processing video: {video_path}")

                cap = cv2.VideoCapture(video_path)
                if not cap.isOpened():
                    print(f"Unable to open video: {video_path}")
                    continue

                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                output_path = os.path.join(self.output_folder, os.path.basename(video_path))
                out = cv2.VideoWriter(output_path, fourcc, 5.0, (640, 480))

                total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                for _ in tqdm(range(total_frames), desc="Processing frames", unit="frame"):
                    ret, frame = cap.read()
                    if not ret:
                        break

                    frame_resized = cv2.resize(frame, (640, 480))
                    results = self.model(frame_resized, verbose=False)

                    if results and hasattr(results[0], 'boxes'):
                        annotated_frame = results[0].plot()
                        out.write(annotated_frame)
                    else:
                        out.write(frame_resized)

                cap.release()
                out.release()
                print(f"Video processed and saved to: {output_path}")

            except Exception as e:
                print(f"Error processing video {video_path}: {e}")
            except KeyboardInterrupt:
                print("Processing interrupted by user.")
                break