import yolov5.train as train; 

def main():
    train.run(data='ped.yaml', imgsz=320, weights='yolov5s.pt',epochs= 1,workers = 12)

if __name__ == "__main__":
    main()