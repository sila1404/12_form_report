import pandas as pd
from utils import get_closing_balance_credit


class F3:
    def __init__(self, file: pd.DataFrame) -> None:
        self.file = file

    def first_report(self):
        report_1 = get_closing_balance_credit(self.file, 51013)
        report_2 = (
            get_closing_balance_credit(self.file, 51021)
            + get_closing_balance_credit(self.file, 51029)
            + get_closing_balance_credit(self.file, 51022)
        )
        total = report_1 + report_2

        return {"total": total, "report_1": report_1, "report_2": report_2}


