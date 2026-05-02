import kagglehub
import pandas as pd
import os

from src.data_loader import data_loader
from src.data_cleaner import data_cleaner
from src.events import monthly_rise_events, monthly_fall_events
from src.metrics import metrics
from src.metrics import (
    min_change, 
    min_change_porcentage, 
    daily_change, 
    weekly_change, 
    monthly_change,
    rolling_avg_weekly, 
    rolling_avg_monthly,
    porcentage_monthly_change
)


dir_path = kagglehub.dataset_download("mczielinski/bitcoin-historical-data")
full_path = os.path.join(dir_path, "btcusd_1-min_data.csv")

if __name__ == '__main__':

    dataset = data_loader(full_path)
    dataset = data_cleaner(dataset)
    dataset = min_change(dataset)
    dataset = min_change_porcentage(dataset)
    dataset = daily_change(dataset)
    dataset = weekly_change(dataset)
    dataset = monthly_change(dataset)
    dataset = rolling_avg_weekly(dataset)
    dataset = rolling_avg_monthly(dataset)
    dataset = porcentage_monthly_change(dataset)
    dataframe_rise = monthly_rise_events(dataset)
    dataframe_fall = monthly_fall_events(dataset)
    
    print(dataframe_rise)
    print("--------------------------------------------")
    print(dataframe_fall)



    