import streamlit as st
from PIL import Image
import pytesseract
import asyncio
import edge_tts
import tempfile
import os

# Cấu hình Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("📸 OCR + Text-to-Speech Web App")
st.write("Upload ảnh, nhận dạng chữ và nghe giọng đọc ngay trên điện thoại.")

# Chọn ngôn ngữ OCR
lang_option = st.selectbox("Chọn ngôn ngữ OCR", ["vie", "eng"])

# Upload ảnh
uploaded_file = st.file_uploader("Chọn ảnh", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Ảnh vừa chọn", use_column_width=True)
    
    # OCR
    text = pytesseract.image_to_string(img, lang=lang_option).strip()
    
    if text:
        st.subheader("📄 Text nhận được")

