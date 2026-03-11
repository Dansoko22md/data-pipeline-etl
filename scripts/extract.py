import pandas as pd

def extract_data(file_path):
    try:
        data = pd.read_csv(file_path)
        if data.empty:
            raise ValueError(f"Le fichier {file_path} est vide.")
        if (data['price'] < 0).any():
            raise ValueError("Certains prix dans le fichier sont négatifs.")
        return data
    except Exception as e:
        print(f"Erreur lors de l'extraction : {e}")
        raise

if __name__ == "__main__":
    df = extract_data("../data/raw_data.csv")
    print(df)
