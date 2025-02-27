# 🚦 TCS-Traffic-Light-System 🚦
## ⚙️ HOW TO RUN? Step by Step Guide ⚙️

### 📝 Circuit Diagram
![Circuit Diagram](circuit-diagram.png)
*This is the circuit diagram for the TCS Traffic Light System*

Note: You will need to upload the circuit diagram image with the filename "circuit-diagram.png" to your repository.

### 📋 Follow These Steps Carefully 📋

# 1️⃣ First Open 'Test 4 - With OCR Rapid API/ Test 4 - Part 3 [Webcam].py' in Pyscripter

# 2️⃣ Second Open Arduino IDE 'Arduino Part\Project TCS\FullCode.ino'

# 3️⃣ Then press win + ← key to align, pyscripter to the left
   * This step is VERY IMPORTANT!

# 4️⃣ Then press win + → key to align, Arduino IDE to the right
   * ⚠️ STEP 3 AND 4 ARE EXTREMELY IMPORTANT! ⚠️

# 5️⃣ If 25 requests has been expired, replace that code as following:
   - 01) First go to this link:
     https://rapidapi.com/api4ai-api4ai-default/api/ocr43
   
   - 02) Copy code (before copy select the code type to Python --> Requests)
   
   - 03) Then click on "Test End-point"
   
   - 04) Select the free plan and subscribe to it. (Free plan only has 25 requests per month)
   
   - 05) ❗IMPORTANT❗: Change the 3rd line of the code to:
     ```python
     files = {"image": open(r"WIN_20240321_09_55_18_Pro.jpg", "rb")}
     ```
     Otherwise code won't work!

# 6️⃣ Upload the code to the arduino board
   * Make sure the correct port is selected

# 7️⃣ If there are any error with LCD screen, upload a sample code to fix it

# 8️⃣ Open the serial monitor (ctrl + shift + m)

# 9️⃣ Then Start the Python Program by pressing F9

## ❗❗ IMPORTANT NOTES ❗❗
- Pyscripter and Arduino IDE should be aligned to left and right
- After pressing the Run(F9) button, Do not press anything
- Do not move or resize windows during operation
- Make sure all hardware connections are properly made

## 🔧 Troubleshooting 🔧
- If Arduino isn't detected, check USB connection
- If OCR isn't working, check if API requests are exhausted
- For LCD issues, check wiring and contrast settings

---
*Created for TCS-Traffic-Light-System*
*https://github.com/Vikasitha444/TCS-Traffic-Light-System-.git*
