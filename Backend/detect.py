# backend/app/detect.py
from ultralytics import YOLO
import numpy as np
import cv2

model = YOLO("models/yolov8n.pt")  # Replace with your trained weights

def detect_objects_cv2(frame, conf=0.4):
    """Runs YOLOv8 on a BGR frame, returns annotated BGR frame."""
    results = model(frame, conf=conf, imgsz=640)
    annotated = results[0].plot()  # RGB format
    return cv2.cvtColor(annotated, cv2.COLOR_RGB2BGR)
