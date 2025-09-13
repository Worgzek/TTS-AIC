# app.py
import streamlit as st
from PIL import Image
import pytesseract
import asyncio
import edge_tts

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
    st.image(img, caption="Ảnh đã upload", use_column_width=True)

    # OCR
    text = pytesseract.image_to_string(img, lang=lang_code).strip()
    st.subheader("Text nhận được:")
    st.write(text if text else "Không phát hiện chữ nào")

    # Hàm TTS async
    async def tts_edge(text_to_read):
        voice = "vi-VN-NamMinhNeural" if lang_code=="vie" else "en-US-GuyNeural"
        communicate = edge_tts.Communicate(text_to_read, voice)
        await communicate.save("output.mp3")

    # Nút phát TTS
    if st.button("Đọc text"):
        if text:
            asyncio.run(tts_edge(text))
            st.audio("output.mp3", format="audio/mp3")
        else:
            st.warning("Không có text để đọc!")
