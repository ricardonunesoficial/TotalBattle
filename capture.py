# capture.py
import mss
import mss.tools
from config import GAME_REGION, REGIONS
import numpy as np
import cv2

def grab_region(region_name: str):
    region = REGIONS[region_name]
    with mss.mss() as sct:
        monitor = {
            "top": GAME_REGION["top"] + region[1],
            "left": GAME_REGION["left"] + region[0],
            "width": region[2],
            "height": region[3],
        }
        img = sct.grab(monitor)
        # Converter para array OpenCV (BGR)
        img_np = np.array(img)
        img_bgr = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)
        return img_bgr
