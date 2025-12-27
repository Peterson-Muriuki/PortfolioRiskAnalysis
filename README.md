# Monte Carlo Portfolio Risk Analysis

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-76b7b2?style=for-the-badge&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![yfinance](https://img.shields.io/badge/yfinance-008000?style=for-the-badge&logo=yahoo&logoColor=white)

This project implements **Modern Portfolio Theory (MPT)** and **risk management techniques** using Python.  
It demonstrates how to simulate correlated stock returns, optimize portfolio weights, and calculate risk metrics such as **Value at Risk (VaR)** and **Expected Shortfall (ES)**.  
The project is packaged with a **Streamlit dashboard** for interactive exploration.


This project implements **Modern Portfolio Theory (MPT)** and **risk management techniques** using Python.  
It demonstrates how to simulate correlated stock returns, optimize portfolio weights, and calculate risk metrics such as **Value at Risk (VaR)** and **Expected Shortfall (ES)**.  
The project is packaged with a **Streamlit dashboard** for interactive exploration.

---

## Features
- **Data Collection**: Download historical stock prices using `yfinance`.
- **Monte Carlo Simulation**: Generate correlated samples with **Cholesky decomposition**.
- **Portfolio Optimization**: Compute **minimum variance portfolio weights**.
- **Risk Metrics**:
  - Value at Risk (VaR) at 95% and 99%
  - Expected Shortfall (Conditional VaR)
  - VaR Backtesting (exceedance counts)
- **Diversification Measures**: Effective Number of Assets (ENB).
- **Visualization**: Correlation heatmaps, distribution plots with VaR/ES cutoffs.
- **Streamlit Dashboard**: Interactive app to explore portfolio risk.

---

## Project Structure
PortfolioRiskAnalysis/
│
├── data/                  # raw stock data
├── notebooks/             # Jupyter notebooks for exploration
├── src/                   # Python modules
│   ├── data_loader.py
│   ├── simulation.py
│   ├── optimization.py
│   ├── risk_metrics.py
│   └── visualization.py
├── app.py                  # Streamlit app
├── requirements.txt        # dependencies
└── README.md               # project overview


---

## Streamlit App
Run locally:
```bash
streamlit run app.py
The app allows you to:

Select tickers

Choose number of Monte Carlo samples

See optimal weights

View VaR and ES metrics

Visualize portfolio risk distribution

** Example Workflow**

Collect returns for GOOGL and XOM.

Simulate 3,000 samples using Cholesky factorization.

Optimize portfolio weights to minimize variance.

Compare risk vs equal‑weighted portfolio.

Compute VaR & ES and visualize tail risk.

Visuals
Correlation heatmap of simulated returns

Distribution of portfolio returns with VaR/ES cutoffs

Risk reduction comparison (equal vs optimal weights)

Insights
Optimal weights reduced portfolio risk by ~12% compared to equal weights.

Effective Number of Assets showed partial diversification (ENB ≈ 1.7).

ES/VaR ratio at 99% confidence revealed moderate tail risk, consistent with equity portfolios.
## Academic Context
This project was developed as part of my MSc in Financial Engineering at WorldQuant University.  
It demonstrates how theoretical concepts in stochastic modeling, optimization, and risk management can be applied to solve practical challenges in portfolio analysis.

Links
GitHub Repo: PortfolioRiskAnalysis

Streamlit App:

License
MIT License
