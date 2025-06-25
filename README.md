# Recommendation

## Overview
This project builds a recommender system to suggest personalized products to users using user-item interaction data. It explores collaborative filtering, matrix factorization, and a hybrid approach incorporating NLP on product descriptions.

## Project Structure
```
.
├── data/
│   ├── interactions.csv
│   └── products.csv
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_collaborative_filtering.ipynb
│   ├── 03_matrix_factorization.ipynb
│   └── 04_hybrid_nlp.ipynb
├── src/
│   ├── utils.py
│   └── nlp_utils.py
└── README.md
```

## Requirements
- Python 3.8+
- pandas, numpy, scikit-learn, matplotlib, seaborn
- surprise
- nltk, scikit-learn (for NLP)

```bash
pip install pandas numpy scikit-learn matplotlib seaborn scikit-surprise nltk
```

## Data Format

**interactions.csv**
| user_id | product_id | rating |
|---------|------------|--------|
| 1       | 101        | 5      |
| 2       | 105        | 4      |

**products.csv**
| product_id | name           | description                  |
|------------|----------------|------------------------------|
| 101        | Wireless Mouse | Ergonomic wireless mouse...  |
| 105        | Gaming Keyboard| Mechanical keyboard...       |

---

## Steps
1. EDA: Analyze user-item data
2. Collaborative Filtering: User-based & Item-based
3. Matrix Factorization: SVD
4. Hybrid Model: Combine content similarity using NLP with collaborative filtering

## Evaluation
- Use RMSE for rating prediction
- Precision@K and Recall@K for ranking

---

## License
MIT
