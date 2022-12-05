from openai_api import *
from text_to_speech import *
from speech_to_text import *

# Record audio and turn it to text
print('Type enter once you finish to record.')
input_text = sp_to_txt()
print(f'The recorded text was : {input_text}')

# Send the text to ChatGPT and return his output text
print('Sending it to ChatGPT now')
text = chatGPT(input_text)

#Turn ChatGPT output text into speech
print(f'Here is the response :')
print(text)
txt_to_sp(text)
