def standardize_columns(df):
    df.columns = df.columns.str.lower().str.strip()
    return df
