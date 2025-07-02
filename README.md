
# 🧠 Real-Time Object Detection using YOLOv4 + Flask

This project implements real-time object detection using **YOLOv4** and **OpenCV**, served via a lightweight **Flask** web app. It downloads the YOLOv4 weights at runtime and allows object detection via webcam, IP camera, or video input. Perfect for deployment on platforms like **Render**.

---

## 🔍 Features

- ✅ Real-time object detection using YOLOv4 (Darknet)
- 🧠 Uses OpenCV's DNN module (no Darknet compilation needed)
- 🔁 Auto-downloads `yolov4.weights` at runtime
- 🌐 Flask app for simple deployment
- 🎥 Supports webcam, IP cam, or local video file
- 🚀 Ready for cloud deployment (Render.com)

---

## 🗂️ Project Structure

```
Object-Detection/
├── app.py                # Flask application with YOLO integration
├── coco.names            # COCO class labels
├── yolov4.cfg            # YOLOv4 model configuration
├── requirements.txt      # Python dependencies
├── download_weights.py   # Script to auto-download yolov4.weights
├── .render.yaml          # Configuration for Render deployment
├── .gitignore            # Prevents large/binary files from being tracked
└── README.md             # Project documentation (this file)
```

---

## ⚙️ Installation (Local)

### 1. Clone the repository

```bash
git clone https://github.com/Mayank-01x/Object-Detection.git
cd Object-Detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download YOLOv4 weights (if not already downloaded)

```bash
python download_weights.py
```

### 4. Run the app

```bash
python app.py
```

---

## 🎥 Camera Input Options

You can modify `cv2.VideoCapture()` in `app.py`:

```python
# Webcam
cv2.VideoCapture(0)

# IP camera
cv2.VideoCapture("http://your-ip-address:port/video")

# Video file
cv2.VideoCapture("sample_video.mp4")
```

---

## 🌐 Deployment on Render

### 1. Push your repo to GitHub (excluding `yolov4.weights`)

### 2. Go to [https://render.com](https://render.com) and create a new **Web Service**

Use the following settings:

| Setting           | Value                                                           |
|-------------------|-----------------------------------------------------------------|
| **Environment**    | Python                                                         |
| **Build Command**  | `pip install -r requirements.txt && python download_weights.py` |
| **Start Command**  | `python app.py`                                                |

Once deployed, Render will give you a public URL to test your app.

---


## 🙋 Author

**Mayank Aggarwal**  
GitHub: [@Mayank-01x](https://github.com/Mayank-01x/Object-Detection)

---

## 📄 License

This project is licensed under the **MIT License**.

---
