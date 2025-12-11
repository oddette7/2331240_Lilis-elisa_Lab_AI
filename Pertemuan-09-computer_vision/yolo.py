import cv2
from ultralytics import YOLO
import time

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Username atau password RTSP salah")
    exit()

prev_time = time.time()

while True:
    success, frame = cap.read()

    if not success or frame is None:
        print("Gagal membaca frame. coba lagi...")
        cap.release()
        time.sleep(1)
        cap = cv2.VideoCapture(0)
        continue

    # Hitung FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    # YOLO inference
    results = model(frame)
    annotated_frame = results[0].plot()

    # Tambahkan FPS ke video
    cv2.putText(annotated_frame, f"FPS: {int(fps)}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    # Tampilkan hasil
    cv2.imshow("YOLO RTSP CCTV Inference", annotated_frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()