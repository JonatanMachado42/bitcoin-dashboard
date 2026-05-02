import kagglehub
import pandas as pd
import os

dir_path = kagglehub.dataset_download("mczielinski/bitcoin-historical-data")
full_path = os.path.join(dir_path, "btcusd_1-min_data.csv")

def find_files(dir_path):
    for dirname, _, filenames in os.walk(dir_path):
        for filename in filenames:
            print(os.path.join(dirname, filename))


def data_loader(path) -> pd.DataFrame:
    return pd.read_csv(path)
