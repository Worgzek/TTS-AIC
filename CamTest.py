# Import
import pytesseract
from PIL import Image
import asyncio
import edge_tts
import os
import cv2

# Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# TTS
async def tts_edge(text):
    voice = "vi-VN-NamMinhNeural"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("output.mp3")
    os.system("start output.mp3") 

# camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Không mở được camera!")
    exit()

print("Nhấn 'c' để chụp ảnh và đọc text, 'q' để thoát")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không lấy được khung hình")
        break

    cv2.imshow("Camera Live", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'): 
        
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # OCR
        text = pytesseract.image_to_string(img, lang="vie").strip()
        print("Text nhận được từ camera:")
        print(text)

        if text != "":
            # TTS
            asyncio.run(tts_edge(text))
            print("Đã đọc xong!")
        else:
            print("Không phát hiện chữ nào")

    elif key == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()

