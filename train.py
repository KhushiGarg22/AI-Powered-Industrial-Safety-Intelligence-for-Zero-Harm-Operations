from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n.pt")

# Train model
model.train(
    data="../datasets/Hard_hat/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    project="../models",
    name="helmet_detection"
)

print("Training Completed Successfully!")