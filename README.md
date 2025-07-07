# Macro Signal Builder

A comprehensive macroeconomic analysis and investment signal generation system that translates economic indicators into actionable investment insights across major asset classes.

## Project Overview

This project analyzes how macroeconomic indicators can be translated into investment signals for stocks, bonds, currencies, and commodities. It combines real-time data collection, advanced analytics, and an interactive dashboard to help investors make data-driven decisions based on economic conditions.

## Features

### 📊 Interactive Dashboard
- **Real-time Data Visualization**: Charts and metrics for all macroeconomic indicators and asset prices
- **Macro Period Classification**: Automatic labeling of economic conditions (Recession, Expansion, Stagflation, etc.)
- **Performance Analytics**: Historical backtesting of macro-based investment strategies
- **Modern UI**: Beautiful, responsive web interface built with Flask and Chart.js

### 🔄 Automated Data Pipeline
- **Weekly Data Collection**: Automated fetching of FRED (macroeconomic) and Yahoo Finance (market) data
- **Data Processing**: Feature engineering including inflation calculations, GDP growth, volatility measures
- **Error Handling**: Robust error handling and data validation throughout the pipeline
- **Modular Architecture**: Separate scripts for configuration, data fetching, cleaning, and updates

### Investment Logic
- **Macro Period Recognition**: Classifies economic conditions using GDP growth, inflation, and unemployment
- **Asset Class Signals**: Generates buy/sell signals for:
  - **Stocks**: SPY (S&P 500), QQQ (NASDAQ)
  - **Bonds**: TLT (Treasury), HYG (High Yield)
  - **Currency**: UUP (US Dollar)
  - **Commodities**: GLD (Gold)

## Project Structure

```
macro-signal-builder/
├── app.py                 # Flask web application
├── data/                  # Data storage
│   ├── final_dataset.csv  # Main processed dataset
│   ├── macro/            # Individual macro data files
│   └── prices/           # Individual asset price files
├── data_pipeline/        # Automated data collection system
│   ├── config.py         # Configuration and settings
│   ├── fetch_fred.py     # FRED data fetching
│   ├── fetch_yahoo.py    # Yahoo Finance data fetching
│   ├── clean_merge.py    # Data cleaning and feature engineering
│   ├── update_dataset.py # Dataset updates
│   └── pipeline_runner.py # Automated pipeline execution
├── templates/            # HTML templates
├── static/              # CSS, JS, and static assets
├── notebooks/           # Jupyter notebooks for analysis
└── requirements.txt     # Python dependencies
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- Git

### Quick Start
```bash
# Clone the repository
git clone <repository-url>
cd macro-signal-builder

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
python app.py
```

### Data Pipeline Setup
```bash
# Navigate to pipeline directory
cd data_pipeline

# Run the complete pipeline
python pipeline_runner.py

# Or run individual components
python fetch_fred.py      # Fetch macro data
python fetch_yahoo.py     # Fetch market data
python clean_merge.py     # Process and merge data
python update_dataset.py  # Update final dataset
```

## Macroeconomic Indicators

### Primary Indicators
- **GDP Growth**: Overall economic performance and expansion/contraction
- **Inflation (CPI)**: Price level changes and purchasing power
- **Unemployment Rate**: Labor market strength and economic health
- **Federal Funds Rate**: Monetary policy stance and interest rate environment

### Derived Features
- **Inflation Rate**: 12-month percentage change in CPI
- **GDP Growth Rate**: 12-month percentage change in GDP
- **Unemployment Rolling Average**: 6-month moving average
- **Asset Volatility**: 12-month rolling standard deviation
- **Macro Period Classification**: Economic regime identification

## Investment Strategy Logic

### Macro Period Classification
The system automatically classifies economic conditions into:

- **Recession**: GDP growth < 0% or unemployment > 6%
- **Stagflation**: GDP growth < 1.5% and inflation > 4%
- **Overheating**: GDP growth > 3.5%, inflation > 4%, unemployment < 3.5%
- **Expansion**: GDP growth ≥ 2%, inflation ≤ 3%, unemployment < 5%
- **Disinflation**: Inflation < 1%
- **Moderate Growth**: Default category for other conditions

### Asset Class Signals
Based on macro conditions, the system generates signals for:

- **Bonds (TLT)**: Beneficial during economic weakness and falling inflation
- **Stocks (SPY/QQQ)**: Strong performance during expansion with low unemployment
- **Dollar (UUP)**: Strengthens with rising interest rates
- **Gold (GLD)**: Hedge against inflation and economic uncertainty
- **High Yield (HYG)**: Credit-sensitive during economic stress

## 🔄 Data Pipeline

### Automated Weekly Updates
The pipeline runs automatically every week to:
1. **Fetch Latest Data**: Download new macro and market data
2. **Process Features**: Calculate derived indicators and signals
3. **Update Dataset**: Merge new data with historical records
4. **Validate Quality**: Ensure data integrity and completeness

### Data Sources
- **FRED (Federal Reserve)**: GDP, CPI, Unemployment, Federal Funds Rate
- **Yahoo Finance**: Real-time asset prices and historical data

## 📈 Performance Metrics

The system tracks:
- **Macro Period Accuracy**: How well economic conditions are classified
- **Signal Performance**: Historical returns of macro-based strategies
- **Risk Metrics**: Volatility, drawdowns, and Sharpe ratios
- **Correlation Analysis**: Relationships between macro indicators and asset returns

## Usage

### Dashboard Access
1. Start the Flask application: `python app.py`
2. Open your browser to `http://localhost:5000`
3. Explore the interactive charts and metrics

### Data Analysis
- Use Jupyter notebooks in `/notebooks/` for custom analysis
- Access processed data in `/data/final_dataset.csv`
- Run the pipeline manually for custom data updates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit with descriptive messages
5. Push to your branch and create a pull request



**Disclaimer**: This project is for educational and research purposes. 