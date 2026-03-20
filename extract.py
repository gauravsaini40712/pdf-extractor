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
    if len(text.strip()) < 100:
        images = convert_from_path(path)
        for img in images:
            text += pytesseract.image_to_string(img, lang='eng+hin')

    return text
