<div align="center">

# Fine-tuning YOLOv11 with Gradio Inference

    
[![YOLOv11](https://img.shields.io/badge/YOLOv11-Custom-orange)](https://github.com/AlexeyAB/darknet)
[![Ultralytics](https://img.shields.io/badge/Ultralytics-8.3.12-Black?logo=ultralytics&logoColor=white)](https://github.com/ultralytics/yolov5)
[![Gradio](https://img.shields.io/badge/Gradio-4.21.0-FF4B4B?logo=gradio&logoColor=white)](https://gradio.app/)


A fine-tuned YOLOv11 model for detecting cars without license plates, integrated with Gradio for an interactive inference interface.

</div>

## 📌 Introduction
This repository showcases a fine-tuned YOLOv11 model specifically trained to detect license plates of cars. Leveraging the powerful capabilities of YOLOv11 and the ease of use provided by Gradio, we offer a web-based interface for real-time inference.

The dataset was prepared using Roboflow, ensuring that the data is in the correct format for YOLOv11. The model was fine-tuned on this custom dataset to enhance its performance on the specific task of detecting cars without license plates.

<br>

## 📦 Main Technologies
- <strong>YOLOv11</strong> - The latest version of the YOLO object detection model, designed for fast and accurate real-time detection.
- <strong>Roboflow</strong> - A tool for preparing and managing datasets, which was used to format the data for YOLOv11.
- <strong>Gradio</strong> - A Python library for creating UIs for machine learning models, enabling easy sharing and interaction.
- <strong>Python 3.10</strong> - A versatile programming language that allows for the implementation of machine learning and web applications.

<br>

## 📝 Fine-tuning Process

The fine-tuning process involved the following steps:

1. __Data Preparation with Roboflow__: The dataset consisting of images of cars without license plates was prepared using Roboflow. Roboflow was used to annotate the images and export the dataset in the YOLOv11 format.

2. __Model Training__: The pre-trained YOLOv11 model from Ultralytics was fine-tuned on the custom dataset. Training scripts are provided in the src/core/training.py file.

3. __Model Evaluation__: The trained model was evaluated on a validation set to assess its performance. Evaluation metrics and results are available in the runs/train directory.

4. __Inference Interface with Gradio__: Gradio was used to create an interactive web interface for the model, allowing users to upload images and receive predictions in real-time.

<br>

# 📁 Project Structure
The directory structure of the project looks like this:
```
├── checkpoints
│   └── .gitkeep
├── configs
│   └── config.toml
├── data
│   └── .gitkeep
├── images
│   └── test
│       └── car_with_noplate.jpg
├── LICENSE
├── logs
│   └── .gitkeep
├── main.py
├── README.md
├── requirements.txt
├── scripts
│   └── download_data_roboflow.py
└── src
    ├── app.py
    ├── core
    │   ├── inference.py
    │   └── training.py
    ├── pylogger
    │   ├── logger.py
    ├── server
    │   └── server.py
    └── utils
        ├── config.py
        └── logger.py
```

<br>

## 🚀 Quickstart
```bash
# Clone the repository
git clone git@github.com:sh-aidev/yolo-finetuning.git
cd yolo-finetuning

# Install required packages
pip install -r requirements.txt

# Create a .env file and add the following environment variables
# ROBOFLOW_API_KEY=<YOUR_ROBOFLOW_API_KEY>
# MODE=train/infer (for training or inference mode)
# ENVIRONMENT=dev/prod (for logging)

# Download the Roboflow dataset
python scripts/download_data_roboflow.py

# Train the YOLOv11 model
python main.py

# Run the Gradio application
# To run gradio app, set MODE=infer in .env file and change use_pretrained to True in configs/config.toml
python main.py
```
Open your web browser and navigate to http://localhost:7860 to access the Gradio interface.

<br>

## 🖼️ Using the Gradio Interface
The Gradio interface allows you to:

Upload an image of a car.
The model will predict and highlight areas where cars without license plates are detected.
View the output image directly in the browser.

<br>

## 📝 Data Preparation with Roboflow

Roboflow was instrumental in:

- __Annotation__: Efficiently annotating images for the presence of cars without license plates.
- __Dataset Management__: Splitting the dataset into training, validation, and testing sets.
- __Export Formats__: Exporting the dataset in YOLOv11 format, ready for training.

To replicate the data preparation:

1. Sign up on Roboflow.
2. Upload your dataset and perform annotations.
3. Export the dataset in YOLOv11 format.
4. Place the downloaded data into the data directory.

<br>

## 📝 Docker Container Usage Instructions

<strong>Prerequisites</strong>:
- Docker
- Visual Studio Code
- Remote - Containers extension

<strong>Steps</strong>:
1. Clone this repository
2. Open the repository in Visual Studio Code
3. Press Ctrl+Shift+P and select "Remote-Containers: Reopen in Container"
4. Wait for the container to build

## References
- [YOLOv11](https://docs.ultralytics.com/models/yolo11/)
- [Roboflow](https://roboflow.com/)
- [Gradio](https://www.gradio.app/docs)