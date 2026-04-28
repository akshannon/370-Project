import ColorDict
import Desktop

def main():
    first_color = None #color of first item
    coor_color = None #color we are looking for
    second_color = None #color of second item

    ttsp = Desktop()

    # camera take a picture
    # 

    while True:
        if (first_color == None): #haven't chosen first clothing item yet
            rgb = 0 #get RGB from camera
            first_color = ColorDict.get_closest_color(rgb)
            coor_color = ColorDict.get_complement_color(rgb)
            ttsp.first_color(first_color, coor_color)

        rgb2 = 0 #get RGB from camera
        second_color = ColorDict.get_closest_color(rgb2)

        if (second_color != None) and (second_color == coor_color):
            ttsp.found_color_correct(second_color) #print ttsp correct
            break; #Done!
        else:
            ttsp.found_color_incorrect(second_color, coor_color) #incorrect color match
