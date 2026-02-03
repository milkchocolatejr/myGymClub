from pathlib import Path

# Project Constants


DB_PATH = ROOT/ "data" / "gymData.db"
ROOT = Path(__file__).resolve().parents[1]
PORT = 5001
TEMPLATE_PATH = f'{ROOT}/templates'
STATIC_PATH = f'{ROOT}/static'

