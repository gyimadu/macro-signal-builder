import pandas as pd
from fredapi import Fred
from config import FRED_API_KEY, FRED_SERIES, START_DATE, END_DATE

def fetch_fred_data():
    fred = Fred(api_key=FRED_API_KEY)
    data = {}
    for name, series_id in FRED_SERIES.items():
        print(f"Fetching {name} FRED...")
        data[name] = fred.get_series(series_id, observation_start=START_DATE, observation_end=END_DATE)
    df = pd.DataFrame(data)
    df.index.name = "Date"
    df.reset_index(inplace=True)
    df.to_csv("../data/fred_raw.csv", index=False)
    print("Saved to data/fred_raw.csv")

if __name__ == "__main__":
    fetch_fred_data()