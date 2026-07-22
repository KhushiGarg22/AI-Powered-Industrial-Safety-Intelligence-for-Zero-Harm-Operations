from ultralytics import YOLO
import cv2

# Load trained model
model = YOLO("runs/models/helmet_detection-2/weights/best.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("Industrial Safety - Helmet Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()