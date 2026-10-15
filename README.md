<div align="center">

# 📄 DocVision AI

### Production-Style AI Document Intelligence System

**OCR • Document Understanding • Information Extraction • Computer Vision • NLP**

Built using **PyTorch**, **Transformers**, **EasyOCR**, **OpenCV**, **Tesseract**, and **Streamlit**

---

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-red?style=for-the-badge&logo=pytorch)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-ComputerVision-green?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-FF4B4B?style=for-the-badge&logo=streamlit)

</div>

---

# Overview

DocVision AI is an end-to-end **Document Intelligence Pipeline** that extracts structured information from invoices and business documents using modern OCR and document understanding techniques.

The system combines multiple OCR engines with rule-based parsing to automatically identify key business entities such as:

- Invoice Number
- Company Name
- GSTIN
- PAN
- Invoice Date
- Total Amount
- Tax Information

The extracted information is converted into structured JSON for downstream automation workflows.

---

# Architecture

```
                    Document Image
                           │
                           ▼
                 Image Preprocessing
                           │
                           ▼
      ┌─────────────────────────────────┐
      │        OCR Pipeline             │
      │                                 │
      │  • TrOCR                        │
      │  • EasyOCR                      │
      │  • Tesseract                    │
      └─────────────────────────────────┘
                           │
                           ▼
                 Raw Extracted Text
                           │
                           ▼
              Document Parsing Engine
                           │
                           ▼
          Invoice Entity Extraction
                           │
                           ▼
                 Structured JSON Output
                           │
                           ▼
               Streamlit Web Interface
```

---

# Features

## OCR Pipeline

- Multi-engine OCR architecture
- Transformer-based text recognition
- EasyOCR integration
- Tesseract fallback engine
- GPU acceleration support

---

## Document Intelligence

- Invoice parsing
- GSTIN extraction
- PAN detection
- Invoice number recognition
- Date extraction
- Amount extraction
- Business entity recognition

---

## Computer Vision

- Image preprocessing
- Layout analysis
- Bounding region detection
- Document segmentation

---

## Web Application

- Interactive Streamlit interface
- Drag & Drop upload
- OCR visualization
- Structured JSON output

---

# Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Deep Learning | PyTorch |
| Transformers | Hugging Face Transformers |
| OCR | TrOCR, EasyOCR, Tesseract |
| Computer Vision | OpenCV |
| Image Processing | Pillow |
| Frontend | Streamlit |
| Data Processing | NumPy, Pandas |

---

# Project Structure

```
DocVision-AI
│
├── data/
│
├── notebooks/
│
├── reports/
│
├── models/
│
├── src/
│   ├── app.py
│   ├── ocr.py
│   ├── parser.py
│   ├── layout.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/returnzerovicky/DocVision-AI.git
```

Move into the project

```bash
cd DocVision-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Launch the application

```bash
streamlit run src/app.py
```

---

# Sample Output

```json
{
    "business_name": "VK Control System Private Limited",
    "invoice_number": "IN-1",
    "invoice_date": "02-Oct-2024",
    "gstin": "27AAFCV2449G1Z7",
    "pan": "AAFCV2449G",
    "total_amount": "118000.00"
}
```

---

# ML Concepts Demonstrated

- Optical Character Recognition (OCR)
- Transformer-based Vision Models
- Computer Vision
- Information Extraction
- Named Entity Recognition
- Document Layout Understanding
- Rule-based NLP
- Image Processing
- Multi-model AI Pipeline

---

# Future Roadmap

- LayoutLMv3 Integration
- Donut Document Transformer
- PaddleOCR
- Table Structure Recognition
- QR Code Extraction
- Signature Verification
- Multi-language OCR
- Batch Document Processing
- PDF Support
- Vector Database Integration

---

# Applications

- Invoice Automation
- Accounts Payable
- Expense Management
- Financial Document Processing
- Enterprise OCR
- KYC Automation
- Document Digitization
- Intelligent Document Processing (IDP)

---

# Repository Statistics

**Project Type**

Production-style Machine Learning Project

**Domain**

Computer Vision • OCR • Document AI

**Difficulty**

Intermediate → Advanced

---

# Author

## Banoth Vikas

Aspiring AI / ML Engineer

GitHub

https://github.com/returnzerovicky

---

<div align="center">

</div>
