import pandas as pd
import os

def load_dataset(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found")
    try: 
        df = pd.read_csv(path)
        print("Dataset loaded")
        return df
    except Exception as e:
        print(f"Error loading the dataset: {e}")
        return None


def summary(df):
    print("\n Summary:")
    print(f"Shape: {df.shape}")
    print("\nColumns:\n", df.columns.tolist())
    print("\nMissing values:\n", df.isnull().sum())
    print("\nData types:\n", df.dtypes)


if __name__ == "__main__":
    file_path = input("Enter path to your CSV dataset: ")
    df = load_dataset(file_path)
    if df is not None:
        summary(df)
