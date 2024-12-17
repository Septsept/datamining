# Image Manager and YOLO

This project is an image manager that uses the YOLO model to detect and annotate objects in images. It allows you to load a folder of images, display the images, and process the images with YOLO to save the annotated results.

## Features

- Load a folder of images
- Display the list of image paths
- Display each image one by one
- Process images with YOLO and save the annotated results

## Prerequisites

- Python 3.x
- OpenCV
- Ultralytics YOLO

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/septsept/datamining.git
    cd datamining
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the image bank in teams and place it in the root of the project.:

## Usage

1. Run the main script:
    ```bash
    python app.py
    ```

2. Follow the on-screen instructions to interact with the image manager.

## Project Structure

- `app.py`: Main entry point of the program.
- `main.py`: Contains the `Main` class that handles the user interface and interactions.
- `imageBank.py`: Contains the `ImageBank` class for managing images.
- `yoloProcessor.py`: Contains the `YOLOProcessor` class for processing images with YOLO.
- `requirements.txt`: List of required Python dependencies.

## Example Workflow

1. Load a folder of images.
2. Display the list of image paths.
3. Display each image one by one.
4. Process the images with YOLO and save the annotated results in the `image_traitees` folder.

## Author

- Septsept - [GitHub Profile](https://github.com/septsept)
