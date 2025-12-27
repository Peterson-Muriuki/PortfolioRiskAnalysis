# src/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(df, title="Correlation Matrix"):
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title(title)
    plt.show()

def plot_distribution(portfolio_returns, VaR, ES=None):
    sns.histplot(portfolio_returns, bins=50, kde=True)
    plt.axvline(-VaR, color="red", linestyle="--", label=f"VaR")
    if ES:
        plt.axvline(-ES, color="blue", linestyle="--", label=f"ES")
    plt.legend()
    plt.show()
