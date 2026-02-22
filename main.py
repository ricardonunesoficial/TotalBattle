#!/usr/bin/env python3
"""
Total Battle OCR Framework - Integração completa
Monitoriza baús e relatórios → Firestore
"""
import time
import logging
from pathlib import Path
from modules.capture import TotalBattleCapture
from modules.ocr_engine import TotalBattleOCR
from modules.parsers.chests import parse_tb_chests, TBChest
from modules.storage import FirestoreStorage
from config.game_regions import TOTALBATTLE_REGIONS

# Config logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tb_ocr.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TotalBattleOCRMonitor:
    def __init__(self):
        self.capture = TotalBattleCapture(TOTALBATTLE_REGIONS)
        self.ocr = TotalBattleOCR()
        self.storage = FirestoreStorage()
        self.last_chests = set()
    
    def run_cycle(self):
        """Executa um ciclo completo de captura → OCR → parse → storage"""
        try:
            logger.info("=== Iniciando ciclo de monitorização ===")
            
            # 1. Capturar baús do clã
            logger.info("Capturando baús...")
            chests_img = self.capture.grab_region("clan_chests")
            chests_text = self.ocr.extract_chests(chests_img)
            
            if chests_text.strip():
                chests = parse_tb_chests(chests_text)
                if chests:
                    saved = self.storage.save_chests(chests)
                    logger.info(f"✅ {len(saved)} novos baús salvos")
            
            # 2. Capturar relatórios (futuro)
            logger.info("Capturando relatórios...")
            # reports_img = self.capture.grab_region("clan_reports")
            # reports_text = self.ocr.extract_reports(reports_img)
            # reports = parse_reports(reports_text)
            # self.storage.save_reports(reports)
            
            logger.info("✅ Ciclo concluído com sucesso")
            
        except Exception as e:
            logger.error(f"❌ Erro no ciclo: {e}", exc_info=True)
    
    def run(self, interval=60):
        """Loop principal"""
        logger.info("🚀 Total Battle OCR Monitor iniciado")
        logger.info(f"📊 Intervalo: {interval}s")
        
        while True:
            self.run_cycle()
            time.sleep(interval)

if __name__ == "__main__":
    monitor = TotalBattleOCRMonitor()
    monitor.run(interval=60)  # Ajusta conforme necessário
