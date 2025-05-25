from fredapi import Fred
import yfinance as yf
import pandas as pd

FRED_API_KEY = "8fb8b73af03b928be5c33de5d75f7720"

fred = Fred(api_key=FRED_API_KEY)

series_dict = {
    'gdp': 'GDP',
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
    'tlt': 'TLT',
    'gld': 'GLD',
    'hyg': 'HYG',
    'uup': 'UUP',
}

for price_name, price_code in prices_dict.items():
    data = yf.download(price_code, start='2005-05-20', end='2025-05-20', interval='1mo')
    data.to_csv(f'../data/prices/{price_name}.csv')







