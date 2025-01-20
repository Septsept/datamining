# Datamining Project - Image and Video Processing

Welcome to the **Datamining Project**, an advanced image and video processing application leveraging the YOLO model for detecting and annotating objects. This project allows you to manage media files, process them using the YOLO model, and save annotated results for further analysis.

## Features

- **Folder Loading**: Load a folder of images or videos for processing.
- **Media Listing**: Display a sortable list of media paths (images or videos).
- **Media Visualization**:
  - Image: Display images one by one using OpenCV.
  - Video: Stream videos frame by frame in real-time.
- **YOLO Processing**:
  - Detect and annotate images and videos.
  - Save annotated versions in a specified output folder.

## Prerequisites

To use this project, ensure that you have:

- **Python 3.8+** installed on your system.
- Required Python dependencies installed (instructions below).
- A trained YOLO model file (e.g., `yolo11x.pt` or `yolo11n.pt`).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Septsept/datamining.git
    cd datamining
    ```

2. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download a suitable YOLO model and place it in the root of your project or point the processor to the correct model path.

4. Ensure you have image and/or video files:
   - Download the image bank or prepare your folder of media files and place it in the root directory of the project.

## Usage

Run the main application by running `app.py`:

```bash
python app.py
```

### Example Workflow:

1. **Select Media Type**:
   - Choose between image processing or video processing in the app menu.

2. **Load Media**:
   - Load a folder containing image files (`.jpg`, `.png`, etc.) or video files (`.mp4`, `.avi`, etc.).

3. **List Media**:
   - View a list of loaded images or videos with their respective file paths.

4. **Visualize Media**:
   - Display and preview every image or video file to review them before processing.

5. **Process with YOLO**:
   - Process the loaded media with the YOLO model, then save annotated results into the respective output folder (`output/processed_images` or `output/processed_videos`).

## Dependencies

The project requires the following Python libraries:

- `opencv-python` – For image and video processing.
- `ultralytics` – For YOLO model handling.
- `tqdm` – For progress bars during processing.
- `numpy` – (optional) If used implicitly via OpenCV.

You can install these dependencies with:

```bash
pip install -r requirements.txt
```

## Example Results

Check out the `output` folder for:
- Annotated images saved in `processed_images/`.
- Annotated videos saved in `processed_videos/`.