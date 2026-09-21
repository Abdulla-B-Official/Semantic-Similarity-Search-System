import numpy as np


def create_document_vector(tokens, embedding_model):
    word_vectors = [
        embedding_model.wv[word]
        for word in tokens
        if word in embedding_model.wv
    ]

    if not word_vectors:
        return np.zeros(embedding_model.vector_size)

    return np.mean(word_vectors, axis=0)


def create_document_embeddings(tokenized_documents, embedding_model):
    document_embeddings = np.array([
        create_document_vector(tokens, embedding_model)
        for tokens in tokenized_documents
    ])

    return document_embeddings