#coding:utf-8
from ultralytics import YOLO
import cv2

path = 'models/best.pt'
img_path = "TestFiles/4840.jpg"


model = YOLO(path, task='detect')



results = model(img_path)
res = results[0].plot()
res = cv2.resize(res,dsize=None,fx=0.3,fy=0.3,interpolation=cv2.INTER_LINEAR)
cv2.imshow("YOLOv8 Detection", res)
cv2.waitKey(0)