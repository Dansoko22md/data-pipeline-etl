import pandas as pd

def transform_data(df):
    df["price_eur"] = df["price"] * 0.92
    return df

if __name__ == "__main__":
    import sys
    df = pd.read_csv(sys.argv[1])
    df = transform_data(df)
    print(df)
