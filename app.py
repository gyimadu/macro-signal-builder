from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

app = Flask(__name__)

# Load and process data
def load_data():
    df = pd.read_csv('data/final_dataset.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def get_current_signals(df):
    """Generate current investment signals based on latest macro conditions"""
    latest = df.iloc[-1]
    
    # Signal logic based on macro conditions
    signals = {}
    
    # GDP Growth Signal
    if latest['gdp_growth'] > 2.5:
        signals['gdp_signal'] = 'BUY' if latest['unemployment'] < 5 else 'HOLD'
    elif latest['gdp_growth'] < 0:
        signals['gdp_signal'] = 'BUY'  # Bonds typically perform well in recession
    else:
        signals['gdp_signal'] = 'HOLD'
    
    # Inflation Signal
    if latest['Inflation'] > 4:
        signals['inflation_signal'] = 'SELL'  # High inflation hurts bonds
    elif latest['Inflation'] < 1:
        signals['inflation_signal'] = 'BUY'   # Low inflation good for bonds
    else:
        signals['inflation_signal'] = 'HOLD'
    
    # Interest Rate Signal
    if latest['fedFunds'] > 4:
        signals['rate_signal'] = 'BUY'  # High rates attract capital to USD
    else:
        signals['rate_signal'] = 'HOLD'
    
    # Unemployment Signal
    if latest['unemployment'] < 4:
        signals['unemployment_signal'] = 'BUY'  # Low unemployment good for stocks
    elif latest['unemployment'] > 8:
        signals['unemployment_signal'] = 'SELL'  # High unemployment bad for stocks
    else:
        signals['unemployment_signal'] = 'HOLD'
    
    # Asset-specific signals
    asset_signals = {}
    
    # SPY (S&P 500) - Stocks
    spy_score = 0
    if latest['gdp_growth'] > 2: spy_score += 1
    if latest['unemployment'] < 5: spy_score += 1
    if latest['Inflation'] < 3: spy_score += 1
    if latest['fedFunds'] < 3: spy_score += 1
    
    if spy_score >= 3:
        asset_signals['SPY'] = 'BUY'
    elif spy_score <= 1:
        asset_signals['SPY'] = 'SELL'
    else:
        asset_signals['SPY'] = 'HOLD'
    
    # TLT (Bonds)
    tlt_score = 0
    if latest['gdp_growth'] < 1: tlt_score += 1
    if latest['Inflation'] < 2: tlt_score += 1
    if latest['fedFunds'] < 2: tlt_score += 1
    
    if tlt_score >= 2:
        asset_signals['TLT'] = 'BUY'
    elif tlt_score <= 0:
        asset_signals['TLT'] = 'SELL'
    else:
        asset_signals['TLT'] = 'HOLD'
    
    # GLD (Gold)
    gld_score = 0
    if latest['Inflation'] > 3: gld_score += 1
    if latest['fedFunds'] < 1: gld_score += 1
    if latest['gdp_growth'] < 1: gld_score += 1
    
    if gld_score >= 2:
        asset_signals['GLD'] = 'BUY'
    elif gld_score <= 0:
        asset_signals['GLD'] = 'SELL'
    else:
        asset_signals['GLD'] = 'HOLD'
    
    # UUP (Dollar)
    uup_score = 0
    if latest['fedFunds'] > 3: uup_score += 1
    if latest['gdp_growth'] > 2: uup_score += 1
    
    if uup_score >= 1:
        asset_signals['UUP'] = 'BUY'
    else:
        asset_signals['UUP'] = 'HOLD'
    
    return {
        'macro_signals': signals,
        'asset_signals': asset_signals,
        'current_period': latest['Period']
    }

def get_performance_metrics(df):
    """Calculate performance metrics for different economic regimes"""
    metrics = {}
    
    for period in df['Period'].unique():
        period_data = df[df['Period'] == period]
        
        metrics[period] = {
            'spy_avg_return': period_data['spy_returns'].mean(),
            'tlt_avg_return': period_data['tlt_returns'].mean(),
            'gld_avg_return': period_data['gld_returns'].mean(),
            'uup_avg_return': period_data['uup_returns'].mean(),
            'spy_volatility': period_data['spy_volatility'].mean(),
            'tlt_volatility': period_data['tlt_volatility'].mean(),
            'gld_volatility': period_data['gld_volatility'].mean(),
            'uup_volatility': period_data['uup_volatility'].mean(),
            'duration_months': len(period_data)
        }
    
    return metrics

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/current_data')
def current_data():
    df = load_data()
    latest = df.iloc[-1]
    
    current_data = {
        'date': latest['Date'].strftime('%Y-%m-%d'),
        'gdp': round(latest['gdp'], 2),
        'gdp_growth': round(latest['gdp_growth'], 2),
        'inflation': round(latest['Inflation'], 2),
        'unemployment': round(latest['unemployment'], 2),
        'fed_funds': round(latest['fedFunds'], 2),
        'period': latest['Period'],
        'signals': get_current_signals(df)
    }
    
    return jsonify(current_data)

@app.route('/api/historical_data')
def historical_data():
    df = load_data()
    
    # Get date range from query parameters
    start_date = request.args.get('start_date', '2008-01-01')
    end_date = request.args.get('end_date', df['Date'].max().strftime('%Y-%m-%d'))
    
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    
    historical_data = {
        'dates': filtered_df['Date'].dt.strftime('%Y-%m-%d').tolist(),
        'gdp_growth': filtered_df['gdp_growth'].tolist(),
        'inflation': filtered_df['Inflation'].tolist(),
        'unemployment': filtered_df['unemployment'].tolist(),
        'fed_funds': filtered_df['fedFunds'].tolist(),
        'spy_returns': filtered_df['spy_returns'].tolist(),
        'tlt_returns': filtered_df['tlt_returns'].tolist(),
        'gld_returns': filtered_df['gld_returns'].tolist(),
        'uup_returns': filtered_df['uup_returns'].tolist(),
        'periods': filtered_df['Period'].tolist()
    }
    
    return jsonify(historical_data)

@app.route('/api/performance_metrics')
def performance_metrics():
    df = load_data()
    metrics = get_performance_metrics(df)
    return jsonify(metrics)

@app.route('/api/regime_analysis')
def regime_analysis():
    df = load_data()
    
    # Analyze regime transitions
    regime_changes = []
    for i in range(1, len(df)):
        if df.iloc[i]['Period'] != df.iloc[i-1]['Period']:
            regime_changes.append({
                'date': df.iloc[i]['Date'].strftime('%Y-%m-%d'),
                'from_period': df.iloc[i-1]['Period'],
                'to_period': df.iloc[i]['Period'],
                'gdp_growth': round(df.iloc[i]['gdp_growth'], 2),
                'inflation': round(df.iloc[i]['Inflation'], 2),
                'unemployment': round(df.iloc[i]['unemployment'], 2)
            })
    
    return jsonify(regime_changes)

if __name__ == '__main__':
    app.run(debug=True) 