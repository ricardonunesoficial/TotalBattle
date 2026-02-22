#!/usr/bin/env python3
"""
Script para testar e calibrar OCR do Total Battle
"""
from modules.capture import TotalBattleCapture
from modules.ocr_engine import TotalBattleOCR
from modules.parsers.chests import parse_tb_chests
from config.game_regions import TOTALBATTLE_REGIONS
import cv2

def test_full_pipeline():
    capture = TotalBattleCapture(TOTALBATTLE_REGIONS)
    ocr = TotalBattleOCR()
    
    print("🎯 TESTE OCR TOTAL BATTLE")
    print("=" * 50)
    
    # Teste baús
    img = capture.grab_region("clan_chests")
    cv2.imwrite("debug_chests.png", img)
    
    text = ocr.extract_chests(img)
    print("\n📄 TEXTO OCR BRUTO:")
    print(repr(text))
    print("\n📦 BAÚS PARSADOS:")
    
    chests = parse_tb_chests(text)
    for chest in chests:
        print(f"  - {chest.player}: {chest.name} ({chest.source} L{chest.level})")
    
    print(f"\n💾 Total: {len(chests)} baús detectados")
    input("Pressione Enter para sair...")

if __name__ == "__main__":
    test_full_pipeline()
