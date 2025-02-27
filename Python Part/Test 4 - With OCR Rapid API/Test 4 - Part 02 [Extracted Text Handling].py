import json
import pyperclip
import pyautogui


# Sample JSON response
json_response = {
    "results": [{
        "status": {"code": "ok", "message": "Success"},
        "name": "123.jpg",
        "md5": "e7ce18363eba914c627b25fe44cd0558",
        "width": 1280,
        "height": 720,
        "entities": [{
            "kind": "objects",
            "name": "text",
            "objects": [{
                "box": [0.17421875, 0.28888888888888886, 0.45625, 0.7097222222222223],
                "entities": [{
                    "kind": "text",
                    "name": "text",
                    "text": "100\nkm/h\nwww.BaterySigns.is "
                }]
            }]
        }]
    }]
}

# Extracting numbers from the "text" field
for result in json_response["results"]:
    for entity in result["entities"]:
        for obj in entity["objects"]:
            for text_entity in obj["entities"]:
                if text_entity["kind"] == "text":
                    text = text_entity["text"]
                    numbers = [word for word in text.split() if word.isdigit()]
                    print("Numbers:", numbers[0])

                    speed_limit = numbers[0]

                    pyperclip.copy(speed_limit)

                    pyautogui.hotkey('alt', 'tab',)
                    pyautogui.hotkey('ctrl', 'v', 'enter')




