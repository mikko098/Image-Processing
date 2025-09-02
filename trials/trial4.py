import ultralytics
from ultralytics import YOLO

model = YOLO("yolov8s.pt")
results = model(".",save = True, project = "runsv8")