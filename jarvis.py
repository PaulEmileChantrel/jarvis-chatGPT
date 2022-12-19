from openai_api import chatGPT
from text_to_speech import txt_to_sp
from speech_to_text import sp_to_txt
from text_to_speech_microsoft import text_to_speech_ms

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
text_to_speech_ms(text)
