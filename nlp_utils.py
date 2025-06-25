import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def compute_tfidf_matrix(descriptions):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(descriptions)
    return tfidf_matrix, vectorizer