# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# Área do jogo na tela (coordenadas exemplo; ajustar manualmente)
GAME_REGION = {
    "top": 100,   # y
    "left": 100,  # x
    "width": 1280,
    "height": 720,
}

# Sub-regiões específicas (em pixels, relativas ao GAME_REGION)
REGIONS = {
    "chests": (50, 400, 600, 200),      # x, y, w, h
    "reports": (650, 50, 600, 600),
}

# Firestore
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
FIRESTORE_COLLECTION_CHESTS = "chests"
FIRESTORE_COLLECTION_REPORTS = "reports"
