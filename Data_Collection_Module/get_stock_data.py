import yfinance as yf

def fetch_data():
    data = yf.download("AAPL", start="2020-01-01", end="2026-01-01")
    return data

data = fetch_data()
print(data.head())
