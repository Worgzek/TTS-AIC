# OCR to Speech

## 👁 Giới thiệu
Ứng dụng này hỗ trợ người khiếm thị bằng cách:
- Quét văn bản từ hình ảnh (OCR).
- Chuyển văn bản sang giọng nói tiếng Việt tự nhiên (Text-to-Speech).
- Phát file âm thanh ngay lập tức.

## ⚙ Công nghệ sử dụng
- **Python 3.10+**
- **pytesseract** (OCR)
- **Pillow** (xử lý ảnh)
- **edge-tts** (Text to Speech AI, giọng đọc tự nhiên của Microsoft)
- **OpenCV** *(tùy chọn: chụp ảnh từ camera)*

##  cài đặt
1. Python và Tesseract OCR  
   - Tải và cài Tesseract từ: [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)  

2. thư viện cần thiết:
   ```bash
   pip install pytesseract pillow edge-tts opencv-python
