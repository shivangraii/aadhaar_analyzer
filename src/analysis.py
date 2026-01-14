import pandas as pd

def district_trend(df, value_col):
    trend = (
        df.groupby(["district", "date"])[value_col]
        .sum()
        .reset_index()
    )
    return trend


def generate_insights(trend_df):
    low_perf = trend_df.groupby("district")["enrolment_count"].mean()
    threshold = low_perf.mean()
    low_perf = low_perf[low_perf < threshold]

    return low_perf.index.tolist()
