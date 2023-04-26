import os
import openai

openai.api_key="sk-..."

while True:

    prompt = input('\n Escribre un texto: ')

    if prompt == 'salir':
        break

    completion = openai.Completion.create(
        model="text-davinci-003", 
        prompt=prompt,
        max_tokens=2048)
    
    print(completion.choices[0].text)