import yfinance as yf
import pandas as pd
from config import YAHOO_TICKERS, START_DATE, END_DATE

def fetch_yahoo_data():
    all_data = {}
    successful_downloads = 0
    
    for ticker in YAHOO_TICKERS:
        try:
            print(f"Fetching {ticker} from Yahoo Finance...")
            df = yf.download(ticker, start=START_DATE, end=END_DATE, progress=False)
            
            # Check if we got valid data
            if df.empty:
                print(f"  Warning: No data received for {ticker}")
                continue
                
            if "Close" not in df.columns:
                print(f"  Warning: No Close price data for {ticker}")
                continue
                
            # Remove any rows with NaN values in Close price
            df_clean = df["Close"].dropna()
            if df_clean.empty:
                print(f"  Warning: No valid Close prices for {ticker}")
                continue
                
            all_data[ticker] = df_clean
            successful_downloads += 1
            print(f"  Successfully downloaded {len(df_clean)} data points for {ticker}")
            
        except Exception as e:
            print(f"  Error downloading {ticker}: {str(e)}")
            continue
    
    if all_data and successful_downloads > 0:
        print(f"\nCreating DataFrame with {successful_downloads} tickers...")
        
        # Create DataFrame by concatenating all series
        # This ensures proper alignment of dates
        df_final = pd.concat(all_data, axis=1)
        df_final.columns = all_data.keys()  # Set column names to ticker symbols
        df_final.index.name = "Date"
        df_final.reset_index(inplace=True)
        
        df_final.to_csv("../data/yahoo_raw.csv", index=False)
        print(f"Saved {len(df_final)} rows to data/yahoo_raw.csv")
    else:
        print("No valid data was fetched from Yahoo Finance. Check tickers and dates.")

if __name__ == "__main__":
    fetch_yahoo_data()