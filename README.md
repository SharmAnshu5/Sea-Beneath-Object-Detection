# 🌊 Sea Beneath - Real-Time Underwater Object Detection

<p align="center">
  <img src="https://user-images.githubusercontent.com/74359573/173828146-89c7a734-2d6f-4e0a-8f13-55fd6d05d90d.png" width="600"/>
</p>

## 🔍 Overview

**Sea Beneath** is a real-time, deep learning-powered underwater object detection system. Leveraging **YOLOv8** and **Streamlit**, this project enables:
- Real-time detection of underwater objects from live camera input or AUV video feeds.
- Precision/recall/mAP evaluation.
- Training support on custom marine datasets.
- A visually intuitive web interface with Streamlit.
- Deployability for underwater robots and autonomous drones (AUVs).

---

## 🎯 Features

✅ Real-time webcam-based detection  
✅ YOLOv8-based custom-trained model  
✅ 🛸 AUV video feed simulation support  
✅ mAP, precision & recall metric visualization  
✅ Clean, aesthetic Streamlit frontend  
✅ Works offline – No cloud dependency  
✅ Optimized for Indian underwater terrain and marine datasets  
✅ Easily extendable to support VOLO/YOLOv9

---

## 🧠 Tech Stack

| Type        | Tech Used                        |
|-------------|----------------------------------|
| 🎯 Model     | YOLOv8n (Ultralytics)            |
| 🎥 Video I/O | OpenCV                           |
| 🧪 UI        | Streamlit                        |
| 📊 Metrics   | scikit-learn, Matplotlib         |
| 📁 Backend   | FastAPI / Python backend         |
| 📦 Package   | Python 3.10+                     |

---

## 📁 Folder Structure

```
Sea-Beneath-Object-Detection/
│
├── Backend/
│   ├── main.py               # FastAPI backend routes
│   ├── detect.py             # YOLO detection logic
│   ├── train.py              # Training script (optional)
│   ├── metrics.py            # Evaluation metrics
│   ├── utils.py              # Utilities (image preprocessing etc.)
│   └── model/
│       └── yolov8n.pt        # Trained YOLOv8 model
│
├── Frontend/
│   └── app.py                # Streamlit UI
│
├── requirements.txt
└── README.md
```

📸 Sample Detection Output
<p align="center"> <img src="https://user-images.githubusercontent.com/136982632/273436632-7b111805-0ad6-48e6-a813-ccc02a90b749.png" width="600" /> </p>
Underwater object detection with bounding boxes and confidence labels.

---

🚀 How to Run
🧰 Prerequisites

Python 3.10+
```

pip install -r requirements.txt

```
Make sure yolov8n.pt exists in Backend/model/

🔁 Step-by-Step Setup
Clone the repository

```

git clone https://github.com/YourUsername/Sea-Beneath-Object-Detection.git
cd Sea-Beneath-Object-Detection

```
Install dependencies

```
pip install -r requirements.txt
Run Backend (YOLO + FastAPI)
```
```
cd Backend
uvicorn main:app --reload
Run Frontend (Streamlit UI)
In a new terminal:
```
```
cd Frontend
streamlit run app.py

```
---
📊 Evaluation Metrics
Once detection is complete, the system computes:

Precision

Recall

F1 Score

Mean Average Precision (mAP)

These are visualized directly in the UI for transparency and tuning.

🛸 AUV & Real-World Deployment
This system is designed to integrate with:

Underwater Drones (via live video stream input)

AUVs using RTSP feeds or onboard camera streams

Ideal for marine research, surveillance, or disaster response

You can connect a simulated video feed from AUVs or real drone footage into the app easily by modifying:

```

cap = cv2.VideoCapture("auv_video.mp4")  # Replace with 0 for webcam

```
🧠 Training (Optional)
You can retrain the model using train.py on your own marine dataset.

```
python train.py --data custom.yaml --model yolov8n.pt --epochs 50

```
📌 To-Do / Future Plans
 Add VOLO model support

 Switchable model weights from frontend

 SQLite storage for detection logs

 Deploy to web with Streamlit Sharing or Docker

 Add support for satellite-to-submarine sonar coordination

📜 License
This project is licensed under the MIT License.
Feel free to use, modify, and contribute.

👨‍💻 Authors
Anshu Sharma (Backend & AI)
Team Tech AI – 2025 Final Year Project

“Exploring the unseen depths with AI — one frame at a time.”
