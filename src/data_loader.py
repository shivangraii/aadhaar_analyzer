import pandas as pd
import os

def load_multiple_csv(file_paths):
    dataframes = {}
    for path in file_paths:
        name = os.path.basename(path).replace(".csv", "")
        dataframes[name] = pd.read_csv(path)
    return dataframes
