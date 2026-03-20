import pdfplumber
from pdf2image import convert_from_path
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def extract_text(path):
    text = ""

    # Try normal extraction
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"
    except:
        pass

    # If text too small → OCR
   # Disable OCR for now (Render free fix)
if len(text.strip()) < 100:
    text += "\n[OCR not supported on server - only text PDF works]"

    return text
