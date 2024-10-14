from roboflow import Roboflow
import os
from dotenv import load_dotenv

load_dotenv()


rf = Roboflow(api_key=os.environ["ROBOFLOW_KEY"])
project = rf.workspace("yolotest-5vihi").project("no-plate-detection-0rnzl")
version = project.version(1)

# get current directory
current_dir = os.getcwd()

data_dir = os.path.join(current_dir, "data")
print(current_dir)
dataset = version.download("yolov11")

# move No-Plate-Detection-1 folder content to data folder
os.system(f"mv {os.path.join(current_dir, 'No-Plate-Detection-1')}/* {data_dir}")

# remove No-Plate-Detection-1 folder
os.system(f"rm -rf {os.path.join(current_dir, 'No-Plate-Detection-1')}")
