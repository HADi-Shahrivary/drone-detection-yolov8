from ultralytics import YOLO

# Load the trained YOLOv8 model
model = YOLO("best.pt")

# Run inference on a video
results = model.predict(
    source="video 5.mp4",
    show=True,
    save=True,
    conf=0.2,
    imgsz=640
)

print("Detection completed successfully.")
