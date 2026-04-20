import numpy as np

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


# finds the nearest neighbor in the ACCESSIBLE_COLORS dictionary
def get_closest_color(rgb):
    names = list(ACCESSIBLE_COLORS.keys())
    palette_values = np.array(list(ACCESSIBLE_COLORS.values()))
    
    # use euclidean distance
    distances = np.linalg.norm(palette_values - np.array(rgb), axis=1)
    
    # find the index of the smallest distance
    min_index = np.argmin(distances)
    
    return names[min_index]

# finds the complement color 
def get_complement_color(rgb):
    # calculate the mathematical opposite
    complement_rgb = [255 - val for val in rgb]
    
    # find the closest name for that opposite
    return get_closest_color(complement_rgb)