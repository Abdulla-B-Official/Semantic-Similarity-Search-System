# Semantic Similarity Search System

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-000000?style=for-the-badge&logo=flask&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-FastText_%7C_Word2Vec-FF6F00?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

<p align="center">
  <b>A full-stack Natural Language Processing (NLP) semantic search engine designed to index documents, generate vector embeddings using Word2Vec/FastText, and retrieve contextually similar text via a web application.</b>
</p>

---

## Overview

The **Semantic Similarity Search System** is an end-to-end NLP document retrieval system built to process textual datasets, generate vector representations, and deliver fast semantic matching beyond simple keyword lookups.

The project features a modular Python backend for text tokenization, preprocessing, model training, and embedding calculation, paired with a web application for user interaction:

* **Text Preprocessing & Tokenization:** Cleans and normalizes incoming text documents through custom preprocessing and tokenization modules.
* **Vector Model Training:** Trainable backend supporting both **Word2Vec** and **FastText** architectures to create dense word and document embeddings.
* **Semantic Search Engine:** Ranks documents based on vector distance and similarity scores to deliver contextually relevant search results.
* **Interactive Frontend:** Responsive web interface allowing users to enter search queries and receive ranked document matches in real time.

---

## Directory Structure

```text
Project-5 Semantic Similarity Search System/
├── backend/
│   ├── data/
│   │   └── documents.csv            # Raw dataset containing documents
│   ├── embeddings/
│   ├── document_embeddings.py   # Document vector generation logic
│   ├── models/                      # Saved trained models (.model, .npy)
│   ├── preprocessing/
│   │   ├── text_preprocessor.py     # Text cleaning & normalization
│   │   └── tokenizer.py             # Custom tokenization pipeline
│   ├── search/
│   │   └── search_engine.py         # Similarity scoring & vector retrieval
│   ├── training/
│   │   └── train.py                 # Script to train Word2Vec & FastText models
│   └── config.py                    # Project paths & hyperparameters configuration
├── frontend/
│   ├── css/
│   │   └── style.css                # Web app visual styling
│   ├── js/
│   │   └── script.js                # Frontend API fetch & DOM interaction
│   └── index.html                   # User interface entry point
├── .env                             # Environment variables configuration
├── .gitignore                       # Git exclusion rules
├── app.py                           # Flask web server entry point
├── README.md                        # Documentation
└── requirements.txt                 # Python dependencies
