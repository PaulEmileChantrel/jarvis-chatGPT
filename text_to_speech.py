import pyttsx3

def txt_to_sp(text):
    # Create a text-to-speech engine
    engine = pyttsx3.init()

    # Set the voice to the Jarvis voice
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

        # Speak the text
    engine.say(text)
    engine.runAndWait()
    engine.stop()

#txt_to_sp('This is a test, just to try this voice.')
