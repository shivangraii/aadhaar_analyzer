import seaborn as sns
import matplotlib.pyplot as plt

def enrolment_heatmap(trend_df):
    pivot = trend_df.pivot(
        index="district",
        columns="date",
        values="enrolment_count"
    )

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot, cmap="YlOrRd")
    plt.title("District-wise Aadhaar Enrolment Intensity")
    plt.show()
