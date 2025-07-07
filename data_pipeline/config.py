import datetime

FRED_API_KEY = "8fb8b73af03b928be5c33de5d75f7720"

FRED_SERIES = {
    "gdp": "GDPC1",
    "cpi": "CPIAUCSL",
    "unemployment": "UNRATE",
    "fedFunds": "FEDFUNDS",
}

YAHOO_TICKERS = ["SPY", "QQQ", "TLT", "GLD", "HYG", "UUP"]
START_DATE = "2008-01-01"
# Use yesterday to avoid incomplete data from today's trading day
END_DATE = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")