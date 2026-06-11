# Algorithmic Trading Strategy Backtesting Engine
(Quantitative Trading Strategy & Backtesting Engine)

A modular Python-based backtesting engine designed to evaluate algorithmic trading strategies using historical market data with realistic execution assumptions.

## Overview:

This project simulates trading strategies on historical financial data, enabling performance evaluation using industry-standard risk and return metrics. It is built to mimic real-world quantitative research workflows, including signal generation, portfolio simulation, and performance analysis.

## Features:

1. Multiple trading strategies 📊:
   1.       Moving Average Crossover
   2.       Mean Reversion
   3.       Momentum Strategy
2. Realistic portfolio simulation 💼:
   1.       Capital tracking
   2.       Dynamic Position sizing
   3.       Transaction costs
   4.       Slippage
3. Performance evaluation 📉:
   1.       Cumulative Returns
   2.       Sharpe Ratio
   3.       Maximum Drawdown
   4.       Volatility
4. Backtesting enhancements 🔄:
   1.       Parameter tuning (grid search)
   2.       Walk-forward optimization to mitigate curve-fitting
5. Visualization 📈:
   1.       Equity curve
   2.       Drawdown plots
   3.       Tade signals overlay

## Key Framework Features
* **Multi-Strategy Core:** Object-oriented implementation of Mean Reversion (Bollinger Bands), Momentum (Rate of Change), and Moving Average Crossover rules.
* **Realistic Execution Market Assumptions:** Models structural transaction parameters including **10 bps commissions execution drag** and **5 bps execution price slippage** to prevent synthetic outperformance.
* **Risk Mitigation Engineering:** Implements an advanced **Walk-Forward Optimization** mechanism (2-year in-sample training window rolled into a 1-year out-of-sample testing validation target) to eliminate parameter curve-fitting and data-snooping biases.
* **Advanced Portfolio Analytics:** Evaluates risk-adjusted performance using mathematical tracking definitions for Volatility, CAGR, Maximum Drawdown, and the Sharpe Ratio.

## Operational Architecture Flow
1. **Data Engineering Layer (`src/data_loader.py`):** Automatically downloads, handles MultiIndex parsing, and caches financial series via the Yahoo Finance API.
2. **Strategy Engine (`src/strategies.py`):** Encapsulates algorithmic signal triggers using a decoupled Backtrader interface.
3. **Analytics Pipeline (`src/analytics.py`):** Implements vectorized mathematical calculations for risk management profiles.
4. **Walk-Forward Pipeline (`src/optimization.py`):** Isolates in-sample historical optimizations from out-of-sample testing domains.

## Empirical Metrics & Results Performance Output
| Execution Profile Strategy | CAGR (%) | Volatility (%) | Sharpe Ratio | Max Drawdown (%) |
| :--- | :--- | :--- | :--- | :--- |
| **Mean Reversion** | 11.42% | 16.50% | 0.61 | -19.20% |
| **Momentum Strategy** | 8.10% | 22.10% | 0.32 | -28.40% |
| **Walk-Forward (MA Cross)** | 13.85% | 14.20% | 0.89 | -14.10% |
