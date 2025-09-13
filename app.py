# app.py
import streamlit as st
from PIL import Image
import pytesseract
import os
import subprocess

# Cấu hình Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("OCR + TTS Web App")
st.write("Upload một hình ảnh, nhận diện chữ và nghe đọc bằng giọng nhân tạo.")

# Chọn ngôn ngữ OCR
lang_option = st.selectbox("Chọn ngôn ngữ OCR", ["Vietnamese", "English"])
lang_code = "vie" if lang_option == "Vietnamese" else "eng"

# Upload file ảnh
uploaded_file = st.file_uploader("Upload ảnh (.png, .jpg, .jpeg)", type=["png","jpg","jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Ảnh đã upload", use_container_width=True)  # <-- thay đổi ở đây

    # OCR
    text = pytesseract.image_to_string(img, lang=lang_code).strip()
    st.subheader("Text nhận được:")
    st.write(text if text else "Không phát hiện chữ nào")

    # Nút phát TTS
    if st.button("Đọc text"):
        if text:
            # Chọn giọng đọc
            voice = "vi-VN-NamMinhNeural" if lang_code=="vie" else "en-US-GuyNeural"
            output_file = "output.mp3"
            
            # Gọi edge-tts CLI
            command = f'edge-tts --text "{text}" --voice {voice} --write-media {output_file}'
            subprocess.run(command, shell=True)

            # Phát audio trên web
            st.audio(output_file, format="audio/mp3")
        else:
            st.warning("Không có text để đọc!")

