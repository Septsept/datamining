import os
import cv2
from tqdm import tqdm
from processor.processor import Processor

class VideoProcessor(Processor):
    """
    Class to process videos using YOLO.
    """
    def __init__(self, model_path='yolo11n.pt', output_folder='output/processed_videos'):
        """
        Constructor.
        :param model_path: Path to the YOLO model.
        :param output_folder: Folder to save processed videos.
        """
        super().__init__(model_path, output_folder)

    def process_videos(self, video_paths):
        """
        Process the videos.
        :param video_paths: List of video paths to process.
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
                for _ in tqdm(range(total_frames), desc="Processing frames", unit="frame", dynamic_ncols=True):
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