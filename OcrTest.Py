# Import
import pytesseract
from PIL import Image
import asyncio
import edge_tts
import cv2
import os

# Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# open image
img = Image.open("test.png")

# OCR
text = pytesseract.image_to_string(img, lang="vie")
print(text)

# Edge TTS
async def tts_edge(text):
    # voice = "vi-VN-HoaiMyNeural"
    voice = "vi-VN-NamMinhNeural"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("output.mp3")
    os.system("start output.mp3")

# func
asyncio.run(tts_edge(text))

print("thanh cong")
print(cv2.__version__)


