import pandas as pd
from io import BytesIO


def read_file(file_path: BytesIO | None) -> pd.DataFrame:
    try:
        if file_path:
            df = pd.read_excel(file_path)
            # Format the file to use necessary header
            df.columns = df.iloc[0]
            df = df.drop(df.index[0]).reset_index(drop=True)
            # Safely convert "Account Code" from object to numeric, coercing errors to NaN
            df["Account Code"] = pd.to_numeric(df["Account Code"], errors='coerce')
            # Handle NaN values (e.g., drop or fill them)
            df = df.dropna(subset=["Account Code"]).reset_index(drop=True)
            # Convert "Account Code" to int after handling NaN values
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
