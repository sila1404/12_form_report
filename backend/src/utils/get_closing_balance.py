import pandas as pd


def get_closing_balance_debit(file: pd.DataFrame, ac_code: int) -> int:
    # Filter the DataFrame for the specified account code
    filtered = file[file["Account Code"] == ac_code]

    # Check if any rows were returned
    if not filtered.empty:
        return filtered["Closing Balance Debit"].iloc[0]
    else:
        print(f"Account code {ac_code} not found.")  # Debugging line
        return 0  # or some other default value


def get_closing_balance_credit(file: pd.DataFrame, ac_code: int) -> int:
    # Filter the DataFrame for the specified account code
    filtered = file[file["Account Code"] == ac_code]

    # Check if any rows were returned
    if not filtered.empty:
        return filtered["Closing Balance Credit"].iloc[0]
    else:
        print(f"Account code {ac_code} not found.")  # Debugging line
        return 0  # or some other default value
