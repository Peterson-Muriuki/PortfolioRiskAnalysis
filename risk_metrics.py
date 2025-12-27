# src/risk_metrics.py
import numpy as np

def calculate_portfolio_var(simulated_returns, weights, confidence_levels):
    if isinstance(weights, pd.Series):
        weights = weights.values
    portfolio_returns = simulated_returns.values @ weights
    mean = np.mean(portfolio_returns)
    std = np.std(portfolio_returns, ddof=1)
    VaR = {alpha: -np.percentile(portfolio_returns, (1-alpha)*100) for alpha in confidence_levels}
    return {"portfolio_returns": portfolio_returns, "portfolio_mean": mean, "portfolio_std": std, "VaR": VaR}

def expected_shortfall(portfolio_returns, alpha=0.95):
    var = np.percentile(portfolio_returns, (1-alpha)*100)
    tail_losses = portfolio_returns[portfolio_returns <= var]
    return -np.mean(tail_losses)
