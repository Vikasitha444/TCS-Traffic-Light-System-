import requests
import json

url = "https://ocr43.p.rapidapi.com/v1/results"

files = {"image": open(r"WIN_20240321_09_55_18_Pro.jpg", "rb")}
payload = { "url": "https://storage.googleapis.com/api4ai-static/samples/ocr-1.png" }
headers = {
    "X-RapidAPI-Key": "5cda8d51e7mshd600748ed7e4f2fp18862djsn2fc7d7a1f32f",
    "X-RapidAPI-Host": "ocr43.p.rapidapi.com"
}

response = requests.post(url, data=payload, files=files, headers=headers)

print(response.json())


json_response = response.json()
# Extracting numbers from the "text" field
for result in json_response["results"]:
    for entity in result["entities"]:
        for obj in entity["objects"]:
            for text_entity in obj["entities"]:
                if text_entity["kind"] == "text":
                    text = text_entity["text"]
                    numbers = [word for word in text.split() if word.isdigit()]
                    print("Numbers:", numbers)




