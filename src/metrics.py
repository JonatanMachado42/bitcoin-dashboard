import pandas as pd


def metrics(dataframe: pd.DataFrame) -> pd.DataFrame:
    today_value = dataframe["Close"].iloc[-1]
    max_value = dataframe["Close"].max()
    min_value = dataframe["Close"].min()
    avg_value = dataframe["Close"].mean()
    volatility = dataframe["Close"].std()

    print(f"Today's value: ${today_value}")
    print(f"Max value: ${max_value}")
    print(f"Min value: ${min_value}")
    print(f"Average value: ${avg_value}")
    print(f"Volatility: ${volatility}")

    return today_value, max_value, min_value, avg_value, volatility


def min_change(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe["Change"] = dataframe["Close"].diff()
    return dataframe


def min_change_porcentage(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe["Change_porcentage"] = dataframe["Close"].pct_change() * 100
    return dataframe



def daily_change(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe["Change_daily"] = dataframe["Close"] - dataframe["Close"].shift(1440)
    return dataframe

def weekly_change(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe["Change_weekly"] = dataframe["Close"] - dataframe["Close"].shift(10080)
    return dataframe



def monthly_change(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe["Change_monthly"] = dataframe["Close"] - dataframe["Close"].shift(43200)
    return dataframe

def porcentage_monthly_change(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe_copy = dataframe.copy()
    dataframe_copy["Porcentage_change_monthly"] = (dataframe["Close"] - dataframe["Close"].shift(43200)) / dataframe["Close"].shift(43200) * 100
    return dataframe_copy


def rolling_avg_weekly(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe["rolling_avg_weekly"] = dataframe["Close"].rolling(window=10080).mean()
    return dataframe


def rolling_avg_monthly(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe["rolling_avg_monthly"] = dataframe["Close"].rolling(window=43200).mean()
    return dataframe

