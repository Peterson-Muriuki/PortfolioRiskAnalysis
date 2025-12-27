# src/simulation.py
import numpy as np
import pandas as pd

def generate_correlated_samples_manual_cholesky(n_samples, stock_returns):
    corr = stock_returns.corr().values
    n = corr.shape[0]
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i+1):
            if i == j:
                L[i, j] = np.sqrt(corr[i, i] - np.sum(L[i, :j]**2))
            else:
                L[i, j] = (corr[i, j] - np.sum(L[i, :j]*L[j, :j])) / L[j, j]

    Z = np.random.standard_normal((n, n_samples))
    X = L @ Z
    return pd.DataFrame(X.T, columns=stock_returns.columns)
