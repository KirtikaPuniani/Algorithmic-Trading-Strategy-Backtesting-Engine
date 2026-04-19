#moving average crossover is a classic quant strategy that generates buy and sell signals based on the crossover of two moving 
#averages: a short-term moving average (e.g., 50-day) and a long-term moving average (e.g., 200-day).]

#basic logic is if short MA > long MA then we have a buy signal, and if short MA < long MA then we have a sell signal.

import sys
import os

sys.path.append(os.path.abspath("../Data"))

from get_stock_data import fetch_data
import pandas as pd
data = fetch_data()
data['MA50'] = data['Close'].rolling(window=50).mean()
data['MA200'] = data['Close'].rolling(window=200).mean()

data['signal'] = 0
data['signal'][data['MA50'] > data['MA200']] = 1
data['signal'][data['MA50'] < data['MA200']] = -1