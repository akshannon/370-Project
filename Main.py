import pynput.keyboard.Listener
import ColorDict
import TextToSpeech

def main():
    #start button use pip install pynput
    first_color = None
    coor_color = None #color we are looking for
    second_color = None #second color camera finds

    #if statement for start button
    while True:
        if (first_color == None): #haven't chosen first clothing item yet
            rgb = 0 #get RGB from camera
            first_color = ColorDict.get_closest_color(rgb)
            coor_color = ColorDict.get_complement_color(rgb)
            TextToSpeech.first_color(first_color, coor_color)

        rgb2 = 0 #get RGB from camera
        second_color = ColorDict.get_closest_color(rgb2)

        if (second_color != None) and (second_color == coor_color):
            TextToSpeech.found_color_correct(second_color) #print ttsp correct
            break; #Done!
        else:
            TextToSpeech.found_color_incorrect(second_color, coor_color) #incorrect color match