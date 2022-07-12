## Dependencies
import torch
import cv2
import numpy as np

print("Loaded Dependencies.", '/n')

## Load Model
run_model_path = 'last_drowsy_v2.pt'
model = torch.hub.load('utralytics/yolov5',
                       'custom',
                       path=run_model_path)

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
cap.destroyAllWindows()

print("Released")

