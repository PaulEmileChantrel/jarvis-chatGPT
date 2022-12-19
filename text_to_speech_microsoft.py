'''
  For more samples please visit https://github.com/Azure-Samples/cognitive-services-speech-sdk
'''

import azure.cognitiveservices.speech as speechsdk
from config import api_key

def text_to_speech_ms(text):
    # Creates an instance of a speech config with specified subscription key and service region.
    speech_key = api_key
    service_region = "eastus"

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # Note: the voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"
    

    # use the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    result = speech_synthesizer.speak_text_async(text).get()
    # Check result
    # if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    #     print("Speech synthesized for text [{}]".format(text))
    # elif result.reason == speechsdk.ResultReason.Canceled:
    #     cancellation_details = result.cancellation_details
    #     print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    #     if cancellation_details.reason == speechsdk.CancellationReason.Error:
    #         print("Error details: {}".format(cancellation_details.error_details))

if __name__=="__main__":
    text_to_speech_ms(text = "Hi, this is Jenny")
