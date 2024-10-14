import gradio as gr
import sys, os
from src.utils.logger import logger
from src.utils.config import Config
from src.core.inference import YoloInference
from ultralytics import ASSETS

class YOLOServer:
    def __init__(self, config: Config) -> None:

        self.config = config
        use_checkpoint = self.config.obj_detector.detection_model.use_checkpoint
        checkpoint_dir = os.path.join(os.getcwd(), self.config.obj_detector.training.checkpoints_dir)
        checkpoint_name = self.config.obj_detector.training.checkpoint_name
        if use_checkpoint:
            if not os.path.exists(os.path.join(checkpoint_dir, checkpoint_name)):
                logger.error(f"Checkpoint not found at: {self.config.obj_detector.detection_model.model_name}")
                sys.exit(0)
            else:
                logger.debug(f"Checkpoint found at: {os.path.join(checkpoint_dir, checkpoint_name)}")
                model_name = os.path.join(checkpoint_dir, checkpoint_name)
        else:
            model_name = self.config.obj_detector.detection_model.model_name

        logger.debug(f"Model used for inference: {model_name}")
        self.yolo = YoloInference(model_name)

    def run(self):
        im_inp = gr.Image(type="pil", label="Input Image")
        cnf_thr = gr.Slider(minimum=0, maximum=1, value=0.25, label="Confidence threshold")
        iou_thr = gr.Slider(minimum=0, maximum=1, value=0.45, label="IoU threshold")
        im_out = gr.Image(type="pil", label="Output Image")
        demo = gr.Interface(
            fn=self.yolo.predict,
            inputs=[
                im_inp,
                cnf_thr,
                iou_thr
            ],
            outputs=im_out,
            title="Gradio Demo",
            description="Upload images for inference. The Ultralytics YOLOv8n model is used by default.",
            examples=[
                    [ASSETS / "bus.jpg", 0.25, 0.45],
                    [ASSETS / "zidane.jpg", 0.25, 0.45],
                ]
            )
        try:
            demo.launch(server_name = self.config.obj_detector.server.host, server_port = self.config.obj_detector.server.port)
        except KeyboardInterrupt:
            print("\n")
            logger.error("Keyboard Interrupted...")
            sys.exit(0)
        except Exception as e:
            logger.error(f"Error: {e}")
            sys.exit(0)