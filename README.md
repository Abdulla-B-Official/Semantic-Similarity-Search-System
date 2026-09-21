# Semantic Similarity Search System

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-000000?style=for-the-badge&logo=flask&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-FastText_%7C_Word2Vec-FF6F00?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

<p align="center">
  <b>A full-stack Natural Language Processing (NLP) semantic search engine designed to index documents, generate vector embeddings using Word2Vec/FastText, and retrieve contextually similar text via an interactive web application.</b>
</p>

---

## Overview

**Semantic Similarity Search System** is an end-to-end NLP document retrieval system built to process textual datasets, generate vector representations, and deliver fast semantic matching beyond simple exact keyword lookups.

The project features a modular Python backend for text tokenization, preprocessing, model training, and embedding calculation, paired with an interactive HTML/CSS/JS frontend for seamless user interaction:

* **Text Preprocessing & Tokenization:** Cleans, normalizes, and tokenizes incoming text documents through custom modular preprocessing pipelines.
* **Vector Model Training:** Trainable backend supporting both **Word2Vec** and **FastText** architectures to learn dense word and n-gram vector representations.
* **Document Vector Generation:** Computes dense vector representations for full text documents using trained embedding weights.
* **Semantic Search Engine:** Ranks documents based on vector distance and cosine similarity metrics to deliver contextually relevant search results.
* **Interactive Web Interface:** A lightweight web application allowing users to input queries, execute semantic search, and view ranked document matches in real time.

---

## Language Breakdown

| Language | Primary Usage |
| :--- | :--- |
| **Python** | Core NLP pipeline, custom preprocessing, FastText/Word2Vec embedding, vector similarity search, and Flask API routing |
| **JavaScript** | Asynchronous Fetch API requests, dynamic DOM rendering, and user event handling |
| **CSS** | Custom UI layout styling, dark-mode themes, responsive components, and visual feedback |
| **HTML** | Structural markup for the search interface, query input controls, and result card containers |

---

## Application Features

* **Full-Stack Architecture:** Modular separation between the backend NLP processing engine (`backend/`) and the client-facing web application (`frontend/`).
* **Semantic Retrieval:** Understands underlying context and intent to retrieve relevant documents even when exact words do not overlap.
* **Dual Embeddings Support:** Implements Word2Vec and FastText models to capture semantic relationships and out-of-vocabulary words.
* **Clean & Extendable Codebase:** Designed with distinct modules for configuration, tokenization, training, and search logic.

---

## Repository Structure

```text
Project-5 Semantic Similarity Search System/
├── backend/
│   ├── data/
│   │   └── documents.csv            # Raw dataset containing text documents
│   ├── embeddings/
│   │   ├── __init__.py
│   │   └── document_embeddings.py   # Document vector generation logic
│   ├── models/                      # Saved trained models (.model, .npy)
│   ├── preprocessing/
│   │   ├── __init__.py
│   │   ├── text_preprocessor.py     # Text cleaning & normalization
│   │   └── tokenizer.py             # Custom tokenization pipeline
│   ├── search/
│   │   ├── __init__.py
│   │   └── search_engine.py         # Similarity scoring & vector retrieval
│   ├── training/
│   │   ├── __init__.py
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
├── README.md                        # Project documentation
└── requirements.txt                 # Python dependencies
