import pandas as pd
import json
from io import StringIO

class F02:
    def __init__(self, file: dict[str, any]) -> None:
        file = pd.read_json(StringIO(json.dumps(file)))
        self.file = file

    def __get_closing_balance_debit(self, ac_code: int) -> int:
        # Return the value of "Closing Balance Debit" by using the "Account Code" to find the value
        return self.file[self.file["Account Code"] == ac_code][
            "Closing Balance Debit"
        ].iloc[0]

    def first_report(self) -> dict[str, int]:
        # report_1 = self.__get_closing_balance_debit(1101)
        # report_3 = self.__get_closing_balance_debit(112117)
        # total = report_1 + report_3
        # return {
        #     "total": total,
        #     "report_1": report_1,
        #     "report_3": report_3,
        # }
        return self.file["Account Code"]
