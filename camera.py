import os
import cv2
import threading
from ultralytics import YOLO

# ==================================
# Model Path
# ==================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "runs",
    "detect",
    "train-3",
    "weights",
    "best.pt"
)

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found:\n{MODEL_PATH}")

print("Loading YOLO model...")
model = YOLO(MODEL_PATH)
print("Model Classes:", model.names)


class VideoCamera:

    def __init__(self):

        self.cap = None

        for idx in [0, 1, 2]:

            cap = cv2.VideoCapture(idx)

            if cap.isOpened():

                success, frame = cap.read()

                if success:
                    print(f"Camera opened on index {idx}")
                    self.cap = cap
                    break

                cap.release()

        if self.cap is None:
            raise RuntimeError("Unable to open webcam")

        self.frame = None
        self.lock = threading.Lock()

        threading.Thread(
            target=self.update,
            daemon=True
        ).start()

    def update(self):

        while True:

            success, frame = self.cap.read()

            if not success:
                continue

            try:

                results = model.predict(
                    source=frame,
                    imgsz=640,
                    conf=0.35,
                    verbose=False
                )

                person_count = 0
                helmet_count = 0
                head_count = 0

                for box in results[0].boxes:

                    cls = int(box.cls[0])
                    class_name = model.names[cls]

                    if class_name == "person":
                        person_count += 1

                    elif class_name == "helmet":
                        helmet_count += 1

                    elif class_name == "head":
                        head_count += 1

                print(
                    f"Persons: {person_count} | Helmets: {helmet_count} | Heads: {head_count}"
                )

                annotated_frame = results[0].plot()

                with self.lock:
                    self.frame = annotated_frame.copy()

            except Exception as e:

                print("YOLO Error:", e)

                with self.lock:
                    self.frame = frame.copy()

    def get_frame(self):

        with self.lock:

            if self.frame is None:
                return None

            return self.frame.copy()

    def release(self):

        if self.cap is not None:
            self.cap.release()


camera = VideoCamera()


def generate_frames():

    while True:

        frame = camera.get_frame()

        if frame is None:
            continue

        success, buffer = cv2.imencode(".jpg", frame)

        if not success:
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + buffer.tobytes()
            + b"\r\n"
        )


if __name__ == "__main__":

    while True:

        frame = camera.get_frame()

        if frame is None:
            continue

        cv2.imshow("Industrial Safety AI", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()