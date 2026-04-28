import pyttsx3
#pip install pyttsx3 to install to the system

class TextToSpeech:
    global engine
    engine = pyttsx3.init()
    #add changes to volume, voice, rate, etc as needed

    def first_color(currentColor, colorToFind):
        engine.say(f'This item is {currentColor}, find your next item in the color {colorToFind}')
        engine.runAndWait()

    def found_color_correct(foundColor):
        engine.say(f'The item you chose is {foundColor}! Now your outfit is complete.')
        engine.runAndWait()
    
    def found_color_incorrect(foundColor, colorToFind):
        engine.say(f'The item you chose is {foundColor}, not {colorToFind}. Look for another item that is {colorToFind}.')
        engine.runAndWait()