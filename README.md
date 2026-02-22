tb_ocr_totalbattle/
├── config/
│   ├── __init__.py
│   ├── game_regions.py      # Coordenadas específicas TB
│   └── firebase_config.py   # Config Firestore
├── modules/
│   ├── capture.py
│   ├── preprocess.py
│   ├── ocr_engine.py
│   ├── parsers/
│   │   ├── __init__.py
│   │   ├── chests.py
│   │   └── reports.py
│   └── storage.py
├── utils/
│   ├── logger.py
│   └── deduplication.py
├── main.py
├── test_ocr.py             # Para debug/teste
├── .env
├── requirements.txt
└── README.md
