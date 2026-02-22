# storage.py
from google.cloud import firestore
from config import (
    GOOGLE_APPLICATION_CREDENTIALS,
    GCP_PROJECT_ID,
    FIRESTORE_COLLECTION_CHESTS,
    FIRESTORE_COLLECTION_REPORTS,
)
from parser import Chest, Report

# O SDK usa GOOGLE_APPLICATION_CREDENTIALS para achar o JSON
client = firestore.Client(project=GCP_PROJECT_ID)

def save_chests(chests: list[Chest]):
    col = client.collection(FIRESTORE_COLLECTION_CHESTS)
    batch = client.batch()
    for chest in chests:
        doc_ref = col.document()
        batch.set(
            doc_ref,
            {
                "chest_name": chest.chest_name,
                "source": chest.source,
                "level": chest.level,
                "from_player": chest.from_player,
                "captured_at": chest.captured_at,
            },
        )
    batch.commit()

def save_reports(reports: list[Report]):
    col = client.collection(FIRESTORE_COLLECTION_REPORTS)
    batch = client.batch()
    for report in reports:
        doc_ref = col.document()
        batch.set(
            doc_ref,
            {
                "report_type": report.report_type,
                "description": report.description,
                "player": report.player,
                "created_at": report.created_at,
            },
        )
    batch.commit()
