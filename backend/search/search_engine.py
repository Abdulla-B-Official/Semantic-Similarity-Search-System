import pandas as pd
from gensim.models import FastText
from sklearn.metrics.pairwise import cosine_similarity

from backend.config import (
    DOCUMENTS_DATA_PATH,
    FASTTEXT_MODEL_PATH,
    TOP_RESULTS_COUNT
)

from backend.preprocessing.text_preprocessor import preprocess_text
from backend.preprocessing.tokenizer import tokenize_text
from backend.embeddings.document_embeddings import (
    create_document_embeddings,
    create_document_vector
)


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

fasttext_model = FastText.load(FASTTEXT_MODEL_PATH)

document_embeddings = create_document_embeddings(
    tokenized_documents,
    fasttext_model
)


def search_documents(search_query, top_results_count=TOP_RESULTS_COUNT):
    processed_query = preprocess_text(search_query)
    query_tokens = tokenize_text(processed_query)

    query_vector = create_document_vector(
        query_tokens,
        fasttext_model
    )

    similarity_scores = cosine_similarity(
        [query_vector],
        document_embeddings
    )[0]

    top_document_indices = similarity_scores.argsort()[
        -top_results_count:
    ][::-1]

    search_results = []

    for document_index in top_document_indices:
        document = documents_data.iloc[document_index]

        search_results.append({
            "document_id": str(document["document_id"]),
            "category": str(document["category"]),
            "title": str(document["title"]),
            "content": str(document["content"]),
            "similarity_score": round(
                float(similarity_scores[document_index]),
                4
            )
        })

    return search_results