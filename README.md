# TCS-Traffic-Light-System
## How to Run: Step-by-Step Guide


![Circuit Diagram](The%20circit%20diagram.png)

### Prerequisites
- PyScripter installed
- Arduino IDE installed
- Traffic Control System hardware connected properly

### Setup Steps

#### 1. Open Required Software
- First, open **'Test 4 - With OCR Rapid API/ Test 4 - Part 3 [Webcam].py'** in PyScripter
- Next, open **'Arduino Part\Project TCS\FullCode.ino'** in Arduino IDE

#### 2. Arrange Windows (IMPORTANT)
- Press **Win + ←** key to align PyScripter to the left side of screen
- Press **Win + →** key to align Arduino IDE to the right side of screen
- *Note: Proper window arrangement is crucial for the system to work correctly*

#### 3. OCR API Setup
If 25 requests have been expired, replace the OCR code as follows:

1. Visit [https://rapidapi.com/api4ai-api4ai-default/api/ocr43](https://rapidapi.com/api4ai-api4ai-default/api/ocr43)
2. Select code type: **Python → Requests**
3. Copy the provided code
4. Click on **"Test End-point"**
5. Select the free plan and subscribe (Free plan includes 25 requests per month)
6. **IMPORTANT**: Change the 3rd line of the code to:
   ```python
   files = {"image": open(r"WIN_20240321_09_55_18_Pro.jpg", "rb")}
   ```
   *Without this change, the code will not work properly*

#### 4. Upload Arduino Code
- Connect Arduino board to your computer
- Select the correct board and port in Arduino IDE
- Click the Upload button (→) to load the code to the Arduino board
- If any errors occur with the LCD screen, upload a sample LCD code first to fix initialization issues

#### 5. Begin Operation
- Open the Serial Monitor in Arduino IDE (Ctrl + Shift + M)
- Return to PyScripter and run the Python program (F9)

### Important Notes
- Ensure PyScripter and Arduino IDE remain aligned left and right
- After pressing Run (F9), don't press any other keys or move windows
- The system requires both programs to run simultaneously
- If the OCR API stops working, you may need to renew the subscription or use a different API key

### Troubleshooting
- If communication errors occur, check the serial port settings in both programs
- Verify all hardware connections are secure
- Make sure the webcam is properly connected and recognized
- If Arduino reports LCD errors, try resetting the board or checking the LCD connections

---
*For further assistance, contact me or refer to the project documentation*
