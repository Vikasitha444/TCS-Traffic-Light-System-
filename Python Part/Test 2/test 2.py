import io
import json
import cv2
import numpy as np
import requests


image = r'WIN_20240321_09_54_05_Pro.jpg'
Api_key = "K89471999088957"




img = cv2.imread(image) #image goes herer

# Ocr
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", img, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
              files = {image: file_bytes},
              data = {"apikey": Api_key,
                      "language": "eng"})



result = result.content.decode()
result = json.loads(result)


parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
print(text_detected)



