import prompt
import translate

#Tell about Sun in 100 words
message = input("Print your prompt: ")

reply = prompt.prompt(message)
reply_ru = translate.translate(reply)

print(f"ChatGPT RU: {reply_ru.text}")
print(f"ChatGPT EN: {reply}")