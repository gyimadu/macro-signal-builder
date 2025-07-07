import pandas as pd
import numpy as np

def label_macro_period(row):
    gdp = row['gdp_growth']
    inflation = row['Inflation']
    unemployment = row['unemployment_rolling6']  
    
    if gdp < 0:
        return 'Recession'
    elif gdp < 1.5 and inflation > 4:
        return 'Stagflation'
    elif gdp > 3.5 and inflation > 4 and unemployment < 3.5: 
        return 'Overheating'
    elif gdp >= 2 and inflation <= 3 and unemployment < 5:
        return 'Expansion'
    elif unemployment > 6:  
        return 'Recession' if gdp < 1 else 'Slow Growth'
    elif inflation < 1:
        return 'Disinflation'
    else:
        return 'Moderate Growth'

def clean_and_merge():
    fred = pd.read_csv("../data/fred_raw.csv", parse_dates=["Date"])
    yahoo = pd.read_csv("../data/yahoo_raw.csv", parse_dates=["Date"])

    # forward fill macro data, interpolate stock data
    fred = fred.sort_values("Date").ffill()
    yahoo = yahoo.sort_values("Date").interpolate()

    # merge on date
    merged = pd.merge(fred, yahoo, on="Date", how="inner")

    # Calculate derived features first
    merged["Inflation"] = merged['cpi'].pct_change(periods=12) * 100
    merged["gdp_growth"] = merged["gdp"].pct_change(periods=12) * 100
    merged["unemployment_rolling6"] = merged["unemployment"].rolling(window=6).mean()

    # Calculate asset returns
    for ticker in ["SPY", "QQQ", "TLT", "GLD", "HYG", "UUP"]:
        merged[f"{ticker.lower()}_returns"] = merged[ticker].pct_change() * 100

    # Calculate volatility
    for ticker in ["SPY", "QQQ", "TLT", "GLD", "HYG", "UUP"]:
        merged[f"{ticker.lower()}_volatility"] = merged[f"{ticker.lower()}_returns"].rolling(window=12).std() * np.sqrt(12)

    # Label macro periods (now gdp_growth exists)
    merged["Period"] = merged.apply(label_macro_period, axis=1)

    merged.to_csv("../data/merged.csv", index=False)
    print("Saved merged data to data/merged.csv")

if __name__ == "__main__":
    clean_and_merge()
