# 🧠 Real-Time Object Detection using YOLOv4 + Flask

This project implements real-time object detection using **YOLOv4** and **OpenCV**, served via a **Flask web app**. The YOLO model is loaded at runtime, and results are streamed through a web interface.

---

## 🔍 Features

- 🎯 Uses YOLOv4 (Darknet model) for high-accuracy detection
- 🔁 Auto-downloads `yolov4.weights` at runtime
- 💡 Built with Flask and OpenCV
- 🎥 Detects from webcam, IP camera, or video file
- 🌐 Deployable to cloud (Render.com)

---

## 📁 Project Structure

Object-Detection/
│
├── app.py                # Flask app with object detection
├── yolov4.cfg            # YOLOv4 config
├── coco.names            # COCO class labels
├── requirements.txt      # Python dependencies
├── download_weights.py   # Downloads yolov4.weights if missing
├── .render.yaml          # Render deployment config
├── .gitignore            # Ignores yolov4.weights etc.
└── README.md             # You're here

---

## 🔧 Installation (Local)

1. **Clone the repository**

git clone https://github.com/Mayank-01x/Object-Detection.git
cd Object-Detection

2. **Install dependencies**

pip install -r requirements.txt


3. **Download YOLOv4 weights**

python download_weights.py


4. **Run the app**

python app.py

---

## 🛰️ Deployment (Render)

1. Commit all files **except `yolov4.weights`** (it's too large for GitHub).
2. Push to GitHub (already done ✅).
3. Go to [https://render.com](https://render.com)
4. Create a **new Web Service**:
   - Environment: Python
   - Build command: `pip install -r requirements.txt && python download_weights.py`
   - Start command: `python app.py`
5. Open the public Render URL to view your app live 🎉

---

## ⚙️ Configuration

- To use your **webcam**, set:

cv2.VideoCapture(0)


- To use an **IP camera**, set:

cv2.VideoCapture("http://your-ip:port/video")

- For a **video file**, set:

cv2.VideoCapture("test.mp4")

---

## 📷 Example Detection Output

![YOLOv4 Detection Example](https://pjreddie.com/media/image/yolov3/yolov3.jpg)

---

## 🧠 Credits

- [YOLOv4](https://github.com/AlexeyAB/darknet)
- [OpenCV DNN module](https://docs.opencv.org/master/d6/d0f/group__dnn.html)
- [Flask](https://flask.palletsprojects.com/)
- [COCO dataset](https://cocodataset.org/#home)

---

## 📄 License

MIT License - free to use and modify.

---

## 🙋‍♂️ Author

**Mayank Aggarwal**  
[GitHub: @Mayank-01x](https://github.com/Mayank-01x)
