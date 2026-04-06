import pyttsx3
#pip install pyttsx3 to install to the system

class TextToSpeech:
    engine = pyttsx3.init()
    #add changes to volume, voice, rate, etc as needed

    def firstColor(currentColor, colorToFind):
        engine.say(f'This item is {currentColor}, find your next item in the color {colorToFind}')
        engine.runAndWait()

    def foundColorCorrect(foundColor):
        engine.say(f'The item you chose is {foundColor}! Now your outfit is complete.')
        engine.runAndWait()
    
    def foundColorIncorrect(foundColor, colorToFind):
        engine.say(f'The item you chose is {foundColor}, not {colorToFind}. Look for another item that is {colorToFind}.')
        engine.runAndWait()