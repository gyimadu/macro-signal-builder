## HOW THE PIPELINE WORKS

1. **Configuration**
    Set your FRED API key, tickers, and date range in 'config.py'.

2. **Fetch Data**
    - `fetch_fred.py` downloads macro indicators (GDP, CPI, Une)
    - `fetch_yahoo.py` downloads asset prices (SPY, TLT, GLD, UUP) from Yahoo Finance.

3. **Clean & Feature Engineering:**  
    - `clean_merge.py` merges the new FRED and Yahoo data, and calculates:
    - **Inflation** (from CPI, YoY %)
    - **Unemployment rolling 6** (6-period rolling mean)
    - **GDP growth** (QoQ or as needed)
    - **Asset returns** (percent change)
    - **Volatility** (6-period rolling std of returns)
    - **Regime/Period** (classified by macro conditions)

4. **Update Final Dataset:**  
    - `update_dataset.py` merges the new featured data with your existing `final_dataset.csv`, deduplicates by date, and saves the result.

5. **Automation:**  
    - `pipeline_runner.py` runs the full pipeline and repeats weekly.

---

## 🚀 How to Use

1. **Install dependencies:**
   ```
   pip install pandas yfinance fredapi
   ```

2. **Set up your configuration:**
   - Edit `config.py` with your FRED API key and desired tickers.

3. **Run the pipeline manually:**
    ```
    python data_pipeline/pipeline_runner.py
    ```
    - This will fetch, process, and update your dataset, then sleep for 7 days and repeat.

4. **Check your data:**
   - The main output is `data/final_dataset.csv` (in the project’s `data/` folder).

---

## 🛠️ Customization

- **Add or remove features:**  
  Edit the feature engineering section in `clean_merge.py`.
- **Change regime logic:**  
  Update the `classify_regime` function in `clean_merge.py`.
- **Change tickers or indicators:**  
  Edit `config.py`.

---

## 📝 Notes

- The pipeline is modular: you can run each script individually for debugging.
- All new data is fully featured before merging with your historical dataset.
- The pipeline is designed for weekly automation, but you can run it on demand.

---
