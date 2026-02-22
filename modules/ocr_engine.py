import pytesseract
import cv2
import numpy as np

class TotalBattleOCR:
    def __init__(self):
        # Config específica para fontes do Total Battle
        self.configs = {
            "chests": "--psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789:.- ",
            "reports": "--psm 6",
            "chat": "--psm 7"
        }
    
    def extract_chests(self, img):
        """OCR específico para lista de baús"""
        processed = self._preprocess_chests(img)
        text = pytesseract.image_to_string(processed, config=self.configs["chests"])
        return text.strip()
    
    def extract_reports(self, img):
        """OCR para relatórios"""
        processed = self._preprocess_reports(img)
        text = pytesseract.image_to_string(processed, config=self.configs["reports"])
        return text.strip()
    
    def _preprocess_chests(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Filtros específicos para lista de baús (cores do TB)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (0, 0, 200), (180, 50, 255))  # Texto claro
        gray = cv2.bitwise_and(gray, gray, mask=mask)
        return cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    def _preprocess_reports(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Denoise + contraste para relatórios
        denoised = cv2.fastNlMeansDenoising(gray)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        return clahe.apply(denoised)
