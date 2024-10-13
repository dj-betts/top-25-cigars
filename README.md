
# Cigar Data Analysis Project

This repository contains a set of Jupyter Notebooks focused on analyzing and processing cigar-related data.
Each notebook has a specific purpose, from data extraction and cleaning to exploratory data analysis (EDA) and natural language processing (NLP) on tasting notes.

## Notebooks Overview

### 1. `eda_cigar_aficionado.ipynb`
   - **Purpose**: Conducts exploratory data analysis (EDA) on cigar ratings and details from a dataset.
   - **Key Components**:
     - Defines functions for parsing and cleaning strings, such as extracting cigar details, issue dates, and sizes.
     - Uses a dictionary to standardize country names in the dataset.
     - Attempts to filter for commonly sized cigars with recommendations for optimization.

### 2. `nlp_work.ipynb`
   - **Purpose**: Applies natural language processing (NLP) techniques to analyze tasting notes associated with cigars.
   - **Key Components**:
     - Text Preprocessing: Tokenization, lemmatization, and removal of stop words for tasting notes.
     - Vectorization: Uses `CountVectorizer` to create word frequency vectors.
     - Model Training: Implements classifiers (Naive Bayes and Random Forest) and clusters data using KMeans.
     - Model Evaluation: Assesses model performance using confusion matrices and evaluates clustering with silhouette scores.

### 3. `scraper_cigar_aficionado.ipynb`
   - **Purpose**: A web scraper designed to gather cigar data from the Cigar Aficionado website.
   - **Key Components**:
     - Employs `requests` and `BeautifulSoup` to extract various cigar details, including name, score, length, gauge, and strength.
     - Captures and structures metadata into a dataset, setting it up for further analysis.

## Getting Started

1. Clone the repository to your local machine.
2. Install required packages, such as pandas, numpy, matplotlib, sklearn, nltk, requests, and BeautifulSoup.
3. Run each notebook in order, starting from `scraper_cigar_aficionado.ipynb` to gather data, followed by `eda_cigar_aficionado.ipynb` for exploratory analysis, and finally `nlp_work.ipynb` to conduct NLP on tasting notes.

## Requirements

- Python 3.x
- Jupyter Notebook
- Packages: pandas, numpy, matplotlib, sklearn, nltk, requests, BeautifulSoup

## Usage

These notebooks provide tools for analyzing cigar data, understanding patterns in cigar tasting notes, and building predictive models for cigar ratings.

