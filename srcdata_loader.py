# src/data_loader.py
import yfinance as yf
import pandas as pd

def get_stock_returns(tickers, start="2020-01-01", end="2025-01-01"):
    data = yf.download(tickers, start=start, end=end)["Adj Close"]
    returns = data.pct_change().dropna()
    return returns
