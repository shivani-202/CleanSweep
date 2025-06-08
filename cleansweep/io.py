import pandas as pd
import os
import logging

def load_dataset(path):
    """
    Load CSV file into a pandas DataFrame.
    Logs success or failure.
    """
    if not os.path.exists(path):
        logging.error(f"No such file: {path}")
        raise FileNotFoundError(f"No such file: {path}")

    try:
        df = pd.read_csv(path)
        logging.info(" Dataset loaded successfully.")
        return df
    except Exception as e:
        logging.exception(" Failed to load dataset.")
        raise e
