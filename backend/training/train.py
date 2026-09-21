import os
import pandas as pd
import nltk
from gensim.models import Word2Vec, FastText

from backend.config import (
    DOCUMENTS_DATA_PATH,
    WORD2VEC_MODEL_PATH,
    FASTTEXT_MODEL_PATH
)

from backend.preprocessing.text_preprocessor import preprocess_text
from backend.preprocessing.tokenizer import tokenize_text


def prepare_training_data():
    documents_data = pd.read_csv(DOCUMENTS_DATA_PATH)

    documents_data["search_text"] = (
        documents_data["title"].fillna("")
        + " "
        + documents_data["content"].fillna("")
        + " "
        + documents_data["keywords"].fillna("")
    )

    documents_data["lemmatized_text"] = (
        documents_data["search_text"].apply(preprocess_text)
    )

    tokenized_documents = [
        tokenize_text(text)
        for text in documents_data["lemmatized_text"]
    ]

    return tokenized_documents


def train_word2vec(tokenized_documents):
    word2vec_model = Word2Vec(
        sentences=tokenized_documents,
        vector_size=100,
        window=5,
        min_count=1,
        workers=4,
        sg=1,
        seed=42
    )

    word2vec_model.save(WORD2VEC_MODEL_PATH)

    print("Word2Vec model trained and saved successfully.")


def train_fasttext(tokenized_documents):
    fasttext_model = FastText(
        sentences=tokenized_documents,
        vector_size=100,
        window=5,
        min_count=1,
        workers=4,
        sg=1,
        seed=42
    )

    fasttext_model.save(FASTTEXT_MODEL_PATH)

    print("FastText model trained and saved successfully.")


def main():
    nltk.download("stopwords")
    nltk.download("punkt")
    nltk.download("punkt_tab")
    nltk.download("wordnet")
    nltk.download("omw-1.4")

    os.makedirs(os.path.dirname(WORD2VEC_MODEL_PATH), exist_ok=True)

    tokenized_documents = prepare_training_data()

    train_word2vec(tokenized_documents)
    train_fasttext(tokenized_documents)

    print("Training completed successfully.")


if __name__ == "__main__":
    main()