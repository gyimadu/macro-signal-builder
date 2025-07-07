import time
import subprocess
from datetime import datetime, timedelta

def run_pipeline():
    start_time = time.time()
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting pipeline...")
    subprocess.run(["python3", "fetch_fred.py"])
    subprocess.run(["python3", "fetch_yahoo.py"])
    subprocess.run(["python3", "clean_merge.py"])
    subprocess.run(["python3", "update_dataset.py"])

    end_time = time.time()
    duration = timedelta(seconds=end_time - start_time)
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Pipeline completed in {duration}")

if __name__ == "__main__":
    while True:
        run_pipeline()
        print("Pipeline completed, sleeping for 30 days...")
        time.sleep(60 * 60 * 24 * 30)