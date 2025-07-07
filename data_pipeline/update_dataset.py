import pandas as pd

def update_final_dataset():
    try:
        existing = pd.read_csv("../data/final_dataset.csv", parse_dates=["Date"])
    except FileNotFoundError:
        print("No existing dataset found, creating new one...")
        existing = pd.DataFrame()

    new = pd.read_csv("../data/merged.csv", parse_dates=["Date"])

    if not existing.empty:
        combined = pd.concat([existing, new]).drop_duplicates(subset=["Date"], keep="last").sort_values("Date")
    else:
        combined = new

    combined.to_csv("../data/final_dataset.csv", index=False)
    print("Updated final dataset saved to data/final_dataset.csv")

if __name__ == "__main__":
    update_final_dataset()