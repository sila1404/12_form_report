import pandas as pd


def get_f02_closing_balance(file: pd.DataFrame, ac_code: int) -> int:
    return file[file["Account Code"] == ac_code]["Closing Balance Debit"].iloc[0]
