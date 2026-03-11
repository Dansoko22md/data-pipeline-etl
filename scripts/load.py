import pandas as pd
from sqlalchemy import create_engine
import os

def load_data(df, table_name="sales"):
    db_url = os.getenv("POSTGRES_URL", "postgresql://airflow:airflow@postgres:5432/airflow")
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists="replace", index=False)

if __name__ == "__main__":
    import sys
    df = pd.read_csv(sys.argv[1])
    load_data(df)
