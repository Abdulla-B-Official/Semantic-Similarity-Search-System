import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_FOLDER = os.path.join(BASE_DIR, "backend", "models")
DATA_FOLDER = os.path.join(BASE_DIR, "backend", "data")

WORD2VEC_MODEL_PATH = os.path.join(MODEL_FOLDER, "word2vec_model.model")
FASTTEXT_MODEL_PATH = os.path.join(MODEL_FOLDER, "fasttext_model.model")
DOCUMENTS_DATA_PATH = os.path.join(DATA_FOLDER, "documents.csv")

TOP_RESULTS_COUNT = int(os.getenv("TOP_RESULTS_COUNT", 5))
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 5000))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"