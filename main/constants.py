from pathlib import Path

# Project Constants

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT/ "data" / "gymData.db"
PORT = 5001
TEMPLATE_PATH = f'{ROOT}/templates'
STATIC_PATH = f'{ROOT}/static'

