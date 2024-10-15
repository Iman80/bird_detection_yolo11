<div align="center">

# No Plate Detection with YOLOv11 

    
[![YOLOv11](https://img.shields.io/badge/YOLOv11-Custom-orange)](https://github.com/AlexeyAB/darknet)
[![Ultralytics](https://img.shields.io/badge/Ultralytics-8.3.12-Black?logo=ultralytics&logoColor=white)](https://github.com/ultralytics/yolov5)
[![Gradio](https://img.shields.io/badge/Gradio-4.21.0-FF4B4B?logo=gradio&logoColor=white)](https://gradio.app/)


A customized YOLOv11 model fine-tuned for object detection, integrated with Gradio for a user-friendly inference interface.

</div>

## 📌 Introduction
This repository contains a fine-tuned implementation of the YOLOv11 model integrated with Gradio to provide a web-based interface for real-time object detection. The model is trained using a custom dataset and aims to facilitate easy deployment and user interaction through an intuitive UI.

<br>

## 📦 Main Technologies
- <strong>YOLOv11</strong> - The latest version of the YOLO object detection model, designed for fast and accurate real-time detection.
- <strong>Gradio</strong> - A Python library for creating UIs for machine learning models, enabling easy sharing and interaction.
- <strong>Python 3.10</strong> - A versatile programming language that allows for the implementation of machine learning and web applications.

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
python main.py
Open your web browser and navigate to http://localhost:7860 to access the Gradio interface.
```

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
- [Gradio](https://www.gradio.app/docs)