#moving average crossover is a classic quant strategy that generates buy and sell signals based on the crossover of two moving 
#averages: a short-term moving average (e.g., 50-day) and a long-term moving average (e.g., 200-day).]

#basic logic is if short MA > long MA then we have a buy signal, and if short MA < long MA then we have a sell signal.

import sys
import os
import pandas as pd

data_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Data_Collection_Module")
)             #adding data folder to path for imports

sys.path.append(data_path)

from get_stock_data import fetch_data

data = fetch_data() 

#moving average calculations
data['MA50'] = data['Close'].rolling(window=50).mean()
data['MA200'] = data['Close'].rolling(window=200).mean()

data['signal'] = 0    #initialize signal column with 0

data['signal'][data['MA50'] > data['MA200']] = 1       #buy signal when short MA is greater than long MA
data['signal'][data['MA50'] < data['MA200']] = -1      #sell signal when short MA is less than long MA

print(data.tail())