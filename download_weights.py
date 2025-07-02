import urllib.request
import os

WEIGHTS_URL = "https://pjreddie.com/media/files/yolov4.weights"
WEIGHTS_FILE = "yolov4.weights"

if not os.path.exists(WEIGHTS_FILE):
    print(f"Downloading {WEIGHTS_FILE} from {WEIGHTS_URL}...")
    urllib.request.urlretrieve(WEIGHTS_URL, WEIGHTS_FILE)
    print("Download complete.")
else:
    print(f"{WEIGHTS_FILE} already exists.")
