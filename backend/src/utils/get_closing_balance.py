import pandas as pd


def get_closing_balance_debit(file: pd.DataFrame, ac_code: int) -> int:
    # # # Filter the DataFrame based on the account code
    # filtered_data = file[file["Account Code"] == ac_code]
    
    # # Check if the filtered DataFrame is empty
    # if filtered_data.empty:
    #     print(f"No matching account code found for debit: {ac_code}")
    #     return 0  # or None, or raise a custom error
    
    # # Return the first closing balance debit value
    # return filtered_data["Closing Balance Debit"].iloc[0]
    return file[file["Account Code"] == ac_code]["Closing Balance Debit"].iloc[0]



def get_closing_balance_credit(file: pd.DataFrame, ac_code: int) -> int:
    # # Filter the DataFrame based on the account code
    # filtered_data = file[file["Account Code"] == ac_code]
    
    # # Check if the filtered DataFrame is empty
    # if filtered_data.empty:
    #     print(f"No matching account code found for credit: {ac_code}")
    #     return 0  # or None, or raise a custom error
    
    # # Return the first closing balance credit value
    # return filtered_data["Closing Balance Credit"].iloc[0]
    # return file[file["Account Code"] == ac_code]["Closing Balance Credit"].iloc[0]
    return file["Closing Balance Credit"]

