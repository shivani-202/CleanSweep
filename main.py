import logging
from cleansweep.io import load_dataset
import pandas as pd
import json

# Setup logging
logging.basicConfig(
    filename="cleanbot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def basic_summary(df):
    print("\n SUMMARY:")
    print(f"Shape: {df.shape}")
    print("Columns:", df.columns.tolist())
    print("Missing values:\n", df.isnull().sum())
    print("Data types:\n", df.dtypes)

def save_summary(df, output_path="summary.json"):
    summary = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing_values": df.isnull().sum().to_dict(),
        "data_types": df.dtypes.astype(str).to_dict()
    }

    try:
        with open(output_path, "w") as f:
            json.dump(summary, f, indent=4)
        logging.info(f" Summary saved to {output_path}")
    except Exception as e:
        logging.exception(" Failed to save summary.")
        print(f"Error saving summary: {e}")

if __name__ == "__main__":
    file_path = input("Enter path to your CSV dataset: ")
    try:
        df = load_dataset(file_path)
        basic_summary(df)
        save_summary(df)
    except Exception as e:
        print(f"Error: {e}")
