import ColorDict
import Desktop
import camera

def main():
    rgb = camera.takePicture() # camera take a picture call function
    first_color = ColorDict.get_closest_color(rgb)
    coor_color = ColorDict.get_complement_color(rgb)
    # send color w socket