# ocr_engine.py
import pytesseract
from pytesseract import Output

# Se necessário, configurar path do executável Tesseract:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_text(img, lang="eng"):
    # img é imagem em escala de cinza / threshold
    config = "--psm 6"  # assume bloco de texto uniforme
    text = pytesseract.image_to_string(img, lang=lang, config=config)
    return text
