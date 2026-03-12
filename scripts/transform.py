import pandas as pd
from datetime import datetime

def transform_data(df):
    # Conversion du prix en euros
    df["price_eur"] = df["price"] * 0.92
    
    # Ajout d'une catégorie de prix
    def categorize_price(price):
        if price < 500: return 'Bas de gamme'
        if price < 1500: return 'Milieu de gamme'
        return 'Haut de gamme'
    
    df["price_category"] = df["price"].apply(categorize_price)
    
    # Ajout d'un horodatage de traitement
    df["processed_at"] = datetime.now()
    
    return df

if __name__ == "__main__":
    import sys
    df = pd.read_csv(sys.argv[1])
    df = transform_data(df)
    print(df)
