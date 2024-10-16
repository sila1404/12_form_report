import pandas as pd
from io import BytesIO


def read_file(file_path: BytesIO | None) -> pd.DataFrame:
    try:
        if file_path:
            df = pd.read_excel(file_path)
            # Format the file to use necessary header
            df.columns = df.iloc[0]
            df = df.drop(df.index[0]).reset_index(drop=True)
            # Convert "Account Code" from type object to int
            df["Account Code"] = df["Account Code"].astype(int)
            return df
        else:
            print("No file path provided")
            return pd.DataFrame()

    except FileNotFoundError:
        print("File not found. Please check the file path")
        return pd.DataFrame()

    except Exception as e:
        print(f"An error occured: {e}")
        return pd.DataFrame()
