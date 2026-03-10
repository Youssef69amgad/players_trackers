import cv2 
from ultralytics import YOLO
model = YOLO("yolov10m.pt")
cap = cv2.VideoCapture("mat.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (800, 600))
    results = model.track(frame, persist=True ,tracker="bytetrack.yaml",conf=0.3,iou=0.5)
    annotated_frame = results[0].plot()

    cv2.imshow("Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
