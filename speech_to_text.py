import speech_recognition as sr


def sp_to_txt():
    # Create a speech recognition object
    r = sr.Recognizer()

    # Set the microphone as the audio source
    with sr.Microphone() as source:
      # Adjust the recognition settings
      r.adjust_for_ambient_noise(source)

      # Listen for input from the microphone
      audio = r.listen(source)

    # Convert the audio data to text

    text = r.recognize_google(audio)

    # Print the recognized text
    # print('The speech was : ')
    # print(text)
    return text
