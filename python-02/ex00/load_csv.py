import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        result = pd.read_csv(path)
        print(f"Loading dataset of dimensions {result.shape}\n")
        return result
    except Exception as e:
        print("Error: ", e)