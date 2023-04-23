import train

train.run(data='coco128.yaml', imgsz=320, weights='yolov5m.pt', epochs=1, batch=16)