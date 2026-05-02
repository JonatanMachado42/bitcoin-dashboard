import pandas as pd
from datetime import datetime

def data_cleaner(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe["Date"] = pd.to_datetime(dataframe["Timestamp"], unit="s")
    dataframe = dataframe.sort_values(by=["Date"])

    dataframe = dataframe.dropna(subset=["Date","Close"])

    return dataframe