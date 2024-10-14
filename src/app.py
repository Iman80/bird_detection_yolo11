from src.server.server import YOLOServer
from src.core.training import YOLOTrain
import os
from src.utils.logger import logger
from src.utils.config import Config

class App:
    def __init__(self) -> None:
        root_config_dir = "configs"
        logger.debug(f"Root config dir: {root_config_dir}")
        self.config = Config(root_config_dir)
        logger.debug("Configs Loaded...")

        self.app = YOLOServer(self.config) if os.getenv("MODE", "infer") == "infer" else YOLOTrain(self.config)

    def run(self):
        self.app.run()