from fredapi import Fred
import yfinance as yf
import pandas as pd

FRED_API_KEY = "8fb8b73af03b928be5c33de5d75f7720"

fred = Fred(api_key=FRED_API_KEY)

series_dict = {
    'gdp': 'GDPC1',
    'cpi': 'CPIAUCSL',
    'unemployment': 'UNRATE',
    'fedFunds': 'FEDFUNDS',
}

for series_name, series_code in series_dict.items():
    data = fred.get_series(series_code)
    df = pd.DataFrame(data, columns=[series_name])
    df.index.name = 'Date'
    df.to_csv(f'../data/macro/{series_name}.csv')

prices_dict = {
    'spy': 'SPY',
    'qqq': 'QQQ',
    'tlt': 'TLT',
    'gld': 'GLD',
    'hyg': 'HYG',
    'uup': 'UUP',
}

adj_close_data = []

for price_name, ticker in prices_dict.items():
    data = yf.download(ticker, start='1995-01-01', interval='1mo', auto_adjust=False)
    adj = data[['Adj Close']].rename(columns={'Adj Close': price_name})
    adj_close_data.append(adj)
    data.to_csv(f'../data/prices/{price_name}.csv')

adj_close_df = pd.concat(adj_close_data, axis=1)
adj_close_df.to_csv(f'../data/prices/adj_close.csv')









