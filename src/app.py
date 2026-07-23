import streamlit as st
import tempfile
import os

from ocr import OCRProcessor
from parser import DocumentParser


st.set_page_config(
    page_title="DocVision AI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 DocVision AI")
st.subheader("AI-Powered Document Intelligence using TrOCR + EasyOCR + Tesseract")


uploaded_file = st.file_uploader(
    "Upload Invoice / Receipt / Document",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    st.image(uploaded_file, caption="Uploaded Document", use_container_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:

        tmp.write(uploaded_file.read())

        image_path = tmp.name

    with st.spinner("Running OCR..."):

         ocr = OCRProcessor()

    # Try EasyOCR first
         text = ocr.easyocr(image_path)

    # Fallback to Tesseract if EasyOCR extracts almost nothing
         if len(text.strip()) < 20:
             text = ocr.tesseract(image_path)

    st.success("OCR Completed")

    st.subheader("Extracted Text")

    st.text_area(
        "",
        text,
        height=250
    )

    parser = DocumentParser()

    result = parser.parse(text)

    st.subheader("Extracted Information")

    st.json(result)

    os.remove(image_path)