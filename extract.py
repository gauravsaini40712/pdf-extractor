import pdfplumber
from pdf2image import convert_from_path
import pytesseract

def extract_text(path):
    text = ""

    # Step 1: Try normal PDF text extraction
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print("Error in pdfplumber:", e)

    # Step 2: Disable OCR for Render (temporary)
    if len(text.strip()) < 100:
        text += "\n[OCR not supported on server]"

    return text
