#stocks that went up continue going up, and stocks that went down continue going down. Momentum strategy is based on this idea 
#of price persistence, where we buy assets that have shown strong performance in the past and sell assets that have shown 
#weak performance.

#Momentum Indicator: We can calculate a momentum indicator, such as the rate of change (ROC) or relative strength index (RSI), to 
#identify overbought or oversold conditions. For example, if the RSI is above 70, it may indicate that the stock is overbought 
#and could be due for a pullback, while an RSI below 30 may indicate that the stock is oversold and could be due for a rebound.
# Return = Price(t) / Price(t-n)

import sys
import os
import pandas as pd
import Data_Collection_Module.Data_Collection as dc

data_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Data_Collection_Module")
)             #adding data folder to path for imports

sys.path.append(data_path)
data = dc.collect_data()

class MomentumStrategy:
    def __init__(self, data, window=14):
        self.data = data
        self.window = window

    def calculate_momentum(self):
        self.data['Momentum'] = self.data['Close'] / self.data['Close'].shift(self.window)
        return self.data

    def generate_signals(self):
        self.data['Signal'] = 0
        self.data.loc[self.data['Momentum'] > 1, 'Signal'] = 1  # Buy signal
        self.data.loc[self.data['Momentum'] < 1, 'Signal'] = -1 # Sell signal
        return self.data   
    
if __name__ == "__main__":
    momentum_strategy = MomentumStrategy(data)
    momentum_strategy.calculate_momentum()
    signals = momentum_strategy.generate_signals()
    print(signals[['Close', 'Momentum', 'Signal']].tail())