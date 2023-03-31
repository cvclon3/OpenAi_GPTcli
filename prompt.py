import openai
import json

with open("key.txt", "r") as k:
    key = k.readline()

openai.api_key = key

def prompt(message):
    config = json.loads("gpt_config.json")
    role = config["role"]
    model = config["model"]
    print(role, model)
    return 0

    """messages = []

    #message = input("Print your prompt: ")
    messages.append({"role": "user", "content": message})

    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    reply = chat.choices[0].message.content

    #print(f"ChatGPT: {reply}")
    return reply"""