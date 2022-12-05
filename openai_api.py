import os
import openai


def chatGPT(input_text):
    # Set the API key
    openai.api_key = os.environ['OPENAI_API_KEY']


    # Set the model ID
    model = 'text-davinci-002'

    # Set the input text
    #input_text = 'Hello, how are you today?'

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
      engine=model,
      prompt=input_text,
      max_tokens=128,
      temperature=0.5
    )

    # Print the response from the API
    #print(response['choices'][0]['text'])
    return response['choices'][0]['text']
