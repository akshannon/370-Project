import numpy as np
import cv2

ACCESSIBLE_COLORS = {
    # neutrals
    "White": (255, 255, 255), "Silver": (192, 192, 192), 
    "Light Grey": (211, 211, 211), "Dark Grey": (105, 105, 105), "Black": (0, 0, 0),
    
    # reds/pinks/oranges
    "Red": (255, 0, 0), "Maroon": (128, 0, 0), 
    "Pink": (255, 192, 203), "Hot Pink": (255, 105, 180),
    "Orange": (255, 165, 0), "Peach": (255, 218, 185),
    "Yellow": (255, 255, 0), "Cream": (255, 253, 208),
    
    # greens
    "Lime Green": (50, 205, 50), "Green": (0, 128, 0), 
    "Dark Green": (0, 64, 0), "Olive": (128, 128, 0),
    
    # blues/teals
    "Light Blue": (173, 216, 230), "Sky Blue": (135, 206, 235),
    "Blue": (0, 0, 255), "Navy Blue": (0, 0, 128), "Teal": (0, 128, 128),
    
    # purples
    "Lavender": (230, 230, 250), "Purple": (128, 0, 128), "Deep Purple": (48, 25, 52),
    
    # browns
    "Tan": (210, 180, 140), "Beige": (245, 245, 220), 
    "Brown": (139, 69, 19), "Dark Brown": (61, 43, 31)
}

def get_closest_color(rgb):
    names = list(ACCESSIBLE_COLORS.keys())
    
    # Convert input RGB to LAB
    rgb_array = np.uint8([[rgb]])
    lab_input = cv2.cvtColor(rgb_array, cv2.COLOR_RGB2LAB)[0][0].astype(float)
    
    # Convert palette to LAB
    palette = np.uint8([[list(v) for v in ACCESSIBLE_COLORS.values()]])
    lab_palette = cv2.cvtColor(palette, cv2.COLOR_RGB2LAB)[0].astype(float)
    
    distances = np.linalg.norm(lab_palette - lab_input, axis=1)
    return names[np.argmin(distances)]

def get_complement_color(rgb):
    complement_rgb = [255 - val for val in rgb]
    return get_closest_color(complement_rgb)
