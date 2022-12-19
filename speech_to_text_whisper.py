import speech_recognition as sr
import whisper

def sp_to_txt():
    # Create a speech recognition object
    r = sr.Recognizer()

    # Set the microphone as the audio source
    with sr.Microphone() as source:
      # Adjust the recognition settings
      r.adjust_for_ambient_noise(source)

      # Listen for input from the microphone
      audio = r.listen(source)

    with open("audio_file.wav", "wb") as file:
        file.write(audio.get_wav_data())
    print('recorded')
    #print(audio)
    # Convert the audio data to text
    model = whisper.load_model("base")
    result = model.transcribe("audio_file.wav")
    print(result["text"])
    text = result["text"]
    #text = r.recognize_google(audio)

    # Print the recognized text
    # print('The speech was : ')
    # print(text)
    return text
if __name__=='__main__':

    print(sp_to_txt())
