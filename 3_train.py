from ultralytics import YOLO

if __name__ == "__main__":
    # load a model
    model = YOLO("yolov8n.yaml")
    model = YOLO("yolov8n.pt")

    # train the model
    results = model.train(data="data.yaml", epochs=100)