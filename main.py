import kagglehub
import pandas as pd
import os

from src.data_loader import data_loader
from src.data_cleaner import data_cleaner


dir_path = kagglehub.dataset_download("mczielinski/bitcoin-historical-data")
full_path = os.path.join(dir_path, "btcusd_1-min_data.csv")

if __name__ == '__main__':
    dataset = data_loader(full_path)
    dataset = data_cleaner(dataset)
    

    


    