import pandas as pd


def get_closing_balance_debit(file: pd.DataFrame, ac_code: int) -> int:
    return file[file["Account Code"] == ac_code]["Closing Balance Debit"].iloc[0]

def get_closing_balance_credit(file: pd.DataFrame, ac_code: int) -> int:
    return file[file["Account Code"] == ac_code]["Closing Balance Credit"].iloc[0]
