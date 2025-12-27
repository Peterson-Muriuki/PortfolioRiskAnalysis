# app.py
import streamlit as st
import pandas as pd
from data_loader import get_stock_returns
from simulation import generate_correlated_samples_manual_cholesky
from optimization import calculate_minimum_variance_weights
from risk_metrics import calculate_portfolio_var, expected_shortfall

st.title("Monte Carlo Portfolio Risk Analysis")

tickers = st.text_input("Enter stock tickers (comma separated)", "GOOGL,XOM").split(",")
n_samples = st.slider("Number of Monte Carlo samples", 1000, 10000, 3000)

returns = get_stock_returns(tickers)
simulated = generate_correlated_samples_manual_cholesky(n_samples, returns)
weights = calculate_minimum_variance_weights(simulated)

st.write("Optimal Weights:", weights)

risk = calculate_portfolio_var(simulated, weights, [0.95, 0.99])
st.write("Portfolio Mean:", risk["portfolio_mean"])
st.write("Portfolio Std:", risk["portfolio_std"])
st.write("VaR:", risk["VaR"])

es95 = expected_shortfall(risk["portfolio_returns"], 0.95)
st.write("Expected Shortfall (95%):", es95)
