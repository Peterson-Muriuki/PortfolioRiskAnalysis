# src/optimization.py
import numpy as np
import pandas as pd

def calculate_minimum_variance_weights(simulated_returns):
    cov = simulated_returns.cov().values
    ones = np.ones(cov.shape[0])
    w = np.linalg.solve(cov, ones)
    w /= np.sum(w)
    return pd.Series(w, index=simulated_returns.columns)
