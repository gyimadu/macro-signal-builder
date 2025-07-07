# Macro Signal Dashboard

A comprehensive web-based dashboard for analyzing macroeconomic indicators and generating investment signals across major asset classes.

## 🚀 Features

### 📊 Real-Time Macro Analysis
- **Current Economic Regime**: Displays the current economic period (Stagflation, Recession, Disinflation, Moderate Growth, Expansion, Overheating)
- **Live Macro Indicators**: Real-time GDP growth, inflation, unemployment, and Fed funds rate
- **Interactive Charts**: Time series visualization of macro indicators and asset returns

### 🎯 Investment Signals
- **Macro-Based Signals**: Buy/Sell/Hold signals based on current economic conditions
- **Asset-Specific Recommendations**: Individual signals for SPY (stocks), TLT (bonds), GLD (gold), and UUP (dollar)
- **Signal Logic**: 
  - **GDP Growth**: Positive growth favors stocks, negative growth favors bonds
  - **Inflation**: High inflation hurts bonds, low inflation benefits bonds
  - **Interest Rates**: High rates attract capital to USD
  - **Unemployment**: Low unemployment favors stocks, high unemployment favors bonds

### 📈 Performance Analytics
- **Regime Performance**: Average returns for each asset class by economic regime
- **Historical Analysis**: Performance metrics spanning from 2008 to 2025
- **Regime Transitions**: Analysis of when and why economic periods change

### 🎨 Modern UI/UX
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Interactive Charts**: Hover effects, zoom, and data exploration
- **Real-Time Updates**: Auto-refresh every 5 minutes
- **Professional Styling**: Modern gradient design with smooth animations

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+
- pip package manager

### Quick Start

1. **Clone or navigate to the project directory**
   ```bash
   cd macro-signal-builder
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
macro-signal-builder/
├── app.py                 # Main Flask application
├── data/
│   └── final_dataset.csv  # Macro and asset data
├── templates/
│   └── dashboard.html     # Main dashboard template
├── static/
│   ├── css/
│   │   └── dashboard.css  # Custom styling
│   └── js/
│       └── dashboard.js   # Interactive functionality
├── requirements.txt       # Python dependencies
└── DASHBOARD_README.md    # This file
```

## 🔧 API Endpoints

The dashboard provides several REST API endpoints:

- `GET /` - Main dashboard page
- `GET /api/current_data` - Current macro data and signals
- `GET /api/historical_data` - Historical time series data
- `GET /api/performance_metrics` - Performance by economic regime
- `GET /api/regime_analysis` - Economic regime transitions

## 📊 Data Sources

The dashboard uses the following macroeconomic indicators:
- **GDP Growth**: Overall economic performance
- **Inflation (CPI)**: Price level changes
- **Unemployment Rate**: Labor market strength
- **Fed Funds Rate**: Monetary policy stance

Asset classes analyzed:
- **SPY**: S&P 500 ETF (stocks)
- **TLT**: 20+ Year Treasury Bond ETF (bonds)
- **GLD**: Gold ETF (commodities)
- **UUP**: US Dollar Index ETF (currency)

## 🎯 Investment Logic

### Signal Generation Rules

#### Macro Indicators
1. **GDP Growth Signal**
   - GDP > 2.5% + Unemployment < 5% → BUY (stocks)
   - GDP < 0% → BUY (bonds)
   - Otherwise → HOLD

2. **Inflation Signal**
   - Inflation > 4% → SELL (bonds)
   - Inflation < 1% → BUY (bonds)
   - Otherwise → HOLD

3. **Interest Rate Signal**
   - Fed Funds > 4% → BUY (dollar)
   - Otherwise → HOLD

4. **Unemployment Signal**
   - Unemployment < 4% → BUY (stocks)
   - Unemployment > 8% → SELL (stocks)
   - Otherwise → HOLD

#### Asset-Specific Scoring
Each asset class uses a scoring system based on macro conditions:

**SPY (Stocks)**: +1 point each for GDP > 2%, Unemployment < 5%, Inflation < 3%, Fed Funds < 3%
- Score ≥ 3: BUY
- Score ≤ 1: SELL
- Otherwise: HOLD

**TLT (Bonds)**: +1 point each for GDP < 1%, Inflation < 2%, Fed Funds < 2%
- Score ≥ 2: BUY
- Score ≤ 0: SELL
- Otherwise: HOLD

**GLD (Gold)**: +1 point each for Inflation > 3%, Fed Funds < 1%, GDP < 1%
- Score ≥ 2: BUY
- Score ≤ 0: SELL
- Otherwise: HOLD

**UUP (Dollar)**: +1 point each for Fed Funds > 3%, GDP > 2%
- Score ≥ 1: BUY
- Otherwise: HOLD

## 🎨 Customization

### Styling
Modify `static/css/dashboard.css` to customize:
- Color schemes
- Layout spacing
- Animations
- Responsive breakpoints

### Signal Logic
Update the signal generation functions in `app.py`:
- `get_current_signals()` - Modify macro signal logic
- Asset-specific scoring in the same function

### Charts
Customize charts in `static/js/dashboard.js`:
- Chart types and colors
- Data visualization options
- Interactive features

## 🔍 Usage Examples

### For Portfolio Managers
1. Check current economic regime and macro conditions
2. Review investment signals for each asset class
3. Analyze historical performance by regime
4. Monitor regime transitions for timing decisions

### For Individual Investors
1. Understand current economic environment
2. Get actionable investment recommendations
3. Learn how different assets perform in various economic conditions
4. Track macro trends over time

### For Researchers
1. Analyze regime transition patterns
2. Study asset performance correlations
3. Backtest macro-based strategies
4. Export data via API endpoints

## 🚀 Advanced Features

### Keyboard Shortcuts
- `Ctrl/Cmd + R`: Refresh all data
- `Escape`: Close alerts/modals

### Auto-Refresh
Data automatically refreshes every 5 minutes to ensure current information.

### Responsive Design
The dashboard adapts to different screen sizes:
- Desktop: Full layout with side-by-side charts
- Tablet: Stacked layout with optimized spacing
- Mobile: Single-column layout with touch-friendly controls

## 🔧 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Change port in app.py
   app.run(debug=True, port=5001)
   ```

2. **Data not loading**
   - Ensure `data/final_dataset.csv` exists
   - Check file permissions
   - Verify CSV format

3. **Charts not displaying**
   - Check browser console for JavaScript errors
   - Ensure Chart.js is loading properly
   - Verify API endpoints are responding

### Performance Optimization

For large datasets:
- Implement data pagination
- Add caching for API responses
- Optimize chart rendering with data sampling

## 📈 Future Enhancements

Potential improvements:
- **Real-time data feeds**: Connect to live economic data APIs
- **Portfolio optimization**: Add portfolio construction tools
- **Alert system**: Email/SMS notifications for regime changes
- **Backtesting interface**: Interactive strategy testing
- **Export functionality**: PDF reports and data exports
- **User authentication**: Multi-user support with personalized dashboards

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational and research purposes. Please ensure compliance with any data usage agreements.

## 📞 Support

For questions or issues:
1. Check the troubleshooting section
2. Review the API documentation
3. Examine the source code comments
4. Create an issue in the repository

---

**Note**: This dashboard is for informational purposes only and should not be considered as financial advice. Always conduct your own research and consult with financial professionals before making investment decisions. 