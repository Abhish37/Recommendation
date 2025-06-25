import pandas as pd

def load_interactions(path):
    return pd.read_csv(path)

def load_products(path):
    return pd.read_csv(path)