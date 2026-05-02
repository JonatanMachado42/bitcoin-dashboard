import pandas as pd


def monthly_rise_events(
    dataframe: pd.DataFrame,
    quantile: float = 0.90
) -> pd.DataFrame:
    df = dataframe.copy()
    df = df.sort_values("Date")

    monthly = (
        df.groupby(df["Date"].dt.to_period("M"))
        .agg(
            Start_Date=("Date", "first"),
            End_Date=("Date", "last"),
            Start_Price=("Close", "first"),
            End_Price=("Close", "last"),
        )
        .reset_index(names="Month")
    )

    monthly["Month_Change_Percentage"] = (
        (monthly["End_Price"] - monthly["Start_Price"])
        / monthly["Start_Price"]
        * 100
    )

    upper_threshold = monthly["Month_Change_Percentage"].quantile(quantile)

    monthly["Rise"] = monthly["Month_Change_Percentage"] > upper_threshold

    monthly_rise = monthly[monthly["Rise"]].copy()

    print(f"Upper threshold: {upper_threshold:.2f}%")
    print(f"Events found: {len(monthly_rise)}")

    return monthly_rise.sort_values("Month_Change_Percentage", ascending=False)


def monthly_fall_events(
    dataframe: pd.DataFrame,
    quantile: float = 0.10
) -> pd.DataFrame:
    df = dataframe.copy()
    df = df.sort_values("Date")

    monthly = (
        df.groupby(df["Date"].dt.to_period("M"))
        .agg(
            Start_Date=("Date", "first"),
            End_Date=("Date", "last"),
            Start_Price=("Close", "first"),
            End_Price=("Close", "last"),
        )
        .reset_index(names="Month")
    )

    monthly["Month_Change_Percentage"] = (
        (monthly["End_Price"] - monthly["Start_Price"])
        / monthly["Start_Price"]
        * 100
    )

    lower_threshold = monthly["Month_Change_Percentage"].quantile(quantile)

    monthly["Rise"] = monthly["Month_Change_Percentage"] < lower_threshold

    monthly_rise = monthly[monthly["Rise"]].copy()

    print(f"Lower threshold: {lower_threshold:.2f}%")
    print(f"Events found: {len(monthly_rise)}")

    return monthly_rise.sort_values("Month_Change_Percentage", ascending=False)

