import re

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


english_stopwords = set(stopwords.words("english"))
wordnet_lemmatizer = WordNetLemmatizer()


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text


def remove_stopwords(text):
    words = word_tokenize(text)

    filtered_words = [
        word for word in words
        if word not in english_stopwords
    ]

    return " ".join(filtered_words)


def apply_lemmatization(text):
    words = word_tokenize(text)

    lemmatized_words = [
        wordnet_lemmatizer.lemmatize(word)
        for word in words
    ]

    return " ".join(lemmatized_words)


def preprocess_text(text):
    cleaned_text = clean_text(text)
    stopword_removed_text = remove_stopwords(cleaned_text)
    lemmatized_text = apply_lemmatization(stopword_removed_text)

    return lemmatized_text