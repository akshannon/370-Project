import numpy as np
import cv2

# Dictionary of accessible colors with their RGB values
ACCESSIBLE_COLORS = {
    "White": (255, 255, 255),
    "Light Grey": (211, 211, 211),
    "Dark Grey": (105, 105, 105),
    "Black": (0, 0, 0),
    "Red": (255, 0, 0),
    "Pink": (255, 192, 203),
    "Orange": (255, 165, 0),
    "Yellow": (255, 255, 0),
    "Green": (0, 128, 0),
    "Blue": (0, 0, 255),
    "Navy Blue": (0, 0, 128),
    "Purple": (128, 0, 128),
    "Brown": (139, 69, 19),
    "Beige": (245, 245, 220),
}

def get_closest_color(rgb):
    # Use LAB color space instead of RGB for perceptually accurate distance matching
    # LAB matches how humans see color differences
    names = list(ACCESSIBLE_COLORS.keys())

    # Convert input RGB to LAB
    rgb_array = np.uint8([[rgb]])
    lab_input = cv2.cvtColor(rgb_array, cv2.COLOR_RGB2LAB)[0][0].astype(float)

    # Convert entire color palette to LAB
    palette = np.uint8([[list(v) for v in ACCESSIBLE_COLORS.values()]])
    lab_palette = cv2.cvtColor(palette, cv2.COLOR_RGB2LAB)[0].astype(float)

    # Find the color with the smallest LAB distance to the input
    distances = np.linalg.norm(lab_palette - lab_input, axis=1)
    return names[np.argmin(distances)]

def get_complement_color(rgb):
    # Calculate the mathematical complement (opposite on color wheel)
    complement_rgb = [255 - val for val in rgb]

    names = list(ACCESSIBLE_COLORS.keys())

    # Convert palette to LAB
    palette = np.uint8([[list(v) for v in ACCESSIBLE_COLORS.values()]])
    lab_palette = cv2.cvtColor(palette, cv2.COLOR_RGB2LAB)[0].astype(float)

    # Convert complement RGB to LAB
    rgb_array = np.uint8([[complement_rgb]])
    lab_input = cv2.cvtColor(rgb_array, cv2.COLOR_RGB2LAB)[0][0].astype(float)

    # Return the top 3 closest colors to the complement
    distances = np.linalg.norm(lab_palette - lab_input, axis=1)
    top3_indices = np.argsort(distances)[:3]

    return [names[i] for i in top3_indices]
