import pandas as pd
from utils import get_f02_closing_balance


class F02:
    def __init__(self, file: pd.DataFrame) -> None:
        self.file = file

    def first_report(self) -> dict[str, int]:
        report_1 = get_f02_closing_balance(self.file, 1101)
        report_3 = get_f02_closing_balance(self.file, 112117)
        total = report_1 + report_3
        return {
            "total": total,
            "report_1": report_1,
            "report_3": report_3,
        }
