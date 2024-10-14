from ultralytics import YOLO
from src.utils.logger import logger
from src.utils.config import Config
from src.server.server import YOLOServer
import os

class YOLOTrain():
    def __init__(self, config: Config) -> None:
        self.config = config
        self.model = YOLO(self.config.obj_detector.training.model_name)
        logger.debug(f"Model: {self.config.obj_detector.training.model_name}")
        self.training_params = {
            'data': os.path.join(os.getcwd(), self.config.obj_detector.training.data_dir, self.config.obj_detector.training.data_yaml),
            'epochs': self.config.obj_detector.training.epochs,
            'workers': self.config.obj_detector.training.workers,
            'device': self.config.obj_detector.training.device,
        }
        self.config.obj_detector.detection_model.use_checkpoint = True
        self.server = YOLOServer(self.config)


    def run(self):
        logger.debug("Training the model...")
        self.model.train(**self.training_params)
        logger.debug("Training completed...")

        self.model.save(os.path.join(os.getcwd(), self.config.obj_detector.training.checkpoints_dir, self.config.obj_detector.training.checkpoint_name))
        logger.debug(f"Yolo Model saved at: {os.path.join(os.getcwd(), self.config.obj_detector.training.checkpoints_dir)} and named: {self.config.obj_detector.training.checkpoint_name}")
        
        logger.debug("Starting the server...")
        self.server.run()