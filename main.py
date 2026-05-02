import kagglehub
import pandas as pd
import os

from src.data_loader import data_loader
from src.data_cleaner import data_cleaner
from src.metrics import metrics
from src.metrics import min_change, min_change_porcentage, daily_change, weekly_change, monthly_change

dir_path = kagglehub.dataset_download("mczielinski/bitcoin-historical-data")
full_path = os.path.join(dir_path, "btcusd_1-min_data.csv")

if __name__ == '__main__':
    dataset = data_loader(full_path)
    dataset = data_cleaner(dataset)
    dataset = min_change(dataset)
    dataset = min_change_porcentage(dataset)
    dataset = daily_change(dataset)

    print(metrics(dataset))
    print(dataset.tail())




    