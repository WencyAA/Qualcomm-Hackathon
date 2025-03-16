#coding:utf-8
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
# Use the model
if __name__ == '__main__':
    # Use the model
    results = model.train(data='datasets/TrafficSignData/data.yaml', epochs=50, batch=48)

    # success = model.export(format='onnx')



