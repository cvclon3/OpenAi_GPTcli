import openai

with open("key.txt", "r") as k:
    key = k.readline()

openai.api_key = key

def prompt(message):
    messages = []

    #message = input("Print your prompt: ")
    messages.append({"role": "user", "content": message})

    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    reply = chat.choices[0].message.content

    #print(f"ChatGPT: {reply}")
    return reply