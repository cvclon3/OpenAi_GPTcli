import openai
import requests
import time


with open("key.txt", "r") as k:
    key = k.readline()

openai.api_key = key

response = openai.Image.create(
  prompt="A cute anime girl",
  n=2,
  size="1024x1024"
)

image_url = response["data"][0]["url"]

hash = str(int(time.time()*10000000))
with open(f"./images/image_{hash}", "wb") as img:
    response = requests.get(image_url)
    img.write(response.content)

print(hash)