import pyttsx3 #pip install pyttsx3 to install to the system

# use Samba to do file transfer or put socket here

global engine
engine = pyttsx3.init()
#add changes to volume, voice, rate, etc as needed

def text_To_Speech(currentColor, colorToFind):
    engine.say(f'This item is {currentColor}, you can pair it with {colorToFind}')
    engine.runAndWait()

