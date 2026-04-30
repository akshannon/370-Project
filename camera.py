import cv2
import numpy as np

def getColor(frame, k=6):
    # Convert BGR to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (100, 100))
    pixels = image.reshape(-1, 3)

    lower_threshold = 15
    upper_threshold = 240

    mask = np.all((pixels > lower_threshold) & (pixels < upper_threshold), axis=1)
    filtered_pixels = pixels[mask]

    # Fallback if everything got filtered out
    if len(filtered_pixels) == 0:
        filtered_pixels = pixels

    filtered_pixels = np.float32(filtered_pixels)

    criteria = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
        10,
        1.0
    )

    _, labels, centers = cv2.kmeans(
        filtered_pixels,
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

    # Let camera auto-adjust exposure
    webcam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)

    # Warm up - discard first 10 frames so camera adjusts to lighting
    for _ in range(10):
        webcam.read()

    ret, frame = webcam.read()
    webcam.release()

    if not ret:
        raise RuntimeError("Could not read image from webcam")

    print(f"Raw RGB: {getColor(frame, k=k)}")
    return getColor(frame, k=k)
