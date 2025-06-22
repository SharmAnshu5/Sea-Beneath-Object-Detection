# backend/app/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse, Response
import cv2, numpy as np
from detect import detect_objects_cv2

app = FastAPI()
import itertools

@app.get("/")
def root():
    return {"message": "Underwater Detector running"}

@app.get("/live")
def live_feed():
    def gen():
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret: break
            frame = detect_objects_cv2(frame)
            _, buf = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buf.tobytes() + b'\r\n')
        cap.release()
    return StreamingResponse(gen(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.post("/detect/upload")
async def detect_upload(file: UploadFile = File(...), conf: float = 0.4):
    data = await file.read()
    arr = np.frombuffer(data, np.uint8)
    frame = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    frame = detect_objects_cv2(frame, conf=conf)
    _, buf = cv2.imencode('.jpg', frame)
    return Response(buf.tobytes(), media_type="image/jpeg")
