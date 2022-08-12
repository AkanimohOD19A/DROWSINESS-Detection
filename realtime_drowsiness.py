## Install Dependencies
# !pip install torch
# !pip install cv2
# !pip install numpy
# pip list | grep opencv

## Dependencies
import torch
import cv2
import numpy as np

print("Loaded Dependencies.", '/n')

## Load Model
run_model_path = './last_drowsy_v4.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=run_model_path)

# ('ultralytics/yolov5', 'custom', path='path/to/best.pt', source='local')

print("Loaded Model.", '/n')

## Make Detection
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    results = model(frame)
    cv2.imshow('YOLO', np.squeeze(results.render()))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Released")

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

