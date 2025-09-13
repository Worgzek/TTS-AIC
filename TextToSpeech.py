from gtts import gTTS
import os

# Nhập
text = input("Nhập văn bản cần đọc: ")

# Tạo
tts = gTTS(text=text, lang="vi")
tts.save("output.mp3")
print("Sound Created.")

# Phát
os.system("start output.mp3")




