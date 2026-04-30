import cv2
import numpy as np

def getColor(frame, k=6):
    # Convert BGR to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (100, 100))
    pixels = np.float32(image.reshape(-1, 3))

    criteria = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
        10,
        1.0
    )

    _, labels, centers = cv2.kmeans(
        pixels,
        k,
        None,
        criteria,
        10,
        cv2.KMEANS_RANDOM_CENTERS
    )

    centers = np.uint8(centers)
    counts = np.bincount(labels.flatten())
    dominant_color = centers[np.argmax(counts)]

    return dominant_color.tolist()


def takePicture(camera_index=0, k=6):
    webcam = cv2.VideoCapture(camera_index)

    if not webcam.isOpened():
        raise RuntimeError("Could not open webcam")

    ret, frame = webcam.read()
    webcam.release()

    if not ret:
        raise RuntimeError("Could not read image from webcam")

    rgb = getColor(frame, k=k)
    print(f"Raw RGB: {rgb}")
    return rgb
