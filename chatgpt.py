import openai

openai.api_key = '' #insertar key

while True:
    prompt = input('\nIntroduce una pregunta > ')
    if prompt == 'exit' or prompt=='clear':
        break
    
    completion=openai.Completion.create(engine='text-davinci-003',
                            prompt=prompt,
                            max_tokens=2048)

    print(completion.choices[0].text)
