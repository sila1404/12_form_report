import pandas as pd
from utils import get_closing_balance_credit, get_closing_balance_debit


class F3:
    def __init__(self, file: pd.DataFrame) -> None:
        self.file = file

    def first_report(self):
        report_1 = get_closing_balance_credit(self.file, "51013")
        report_2 = (
            get_closing_balance_credit(self.file, "51021")
            + get_closing_balance_credit(self.file, "51029")
            + get_closing_balance_credit(self.file, "51022")
        )
        self.total_first = report_1 + report_2

        return {"total": self.total_first, "report_1": report_1, "report_2": report_2}

    def second_report(self):
        report_1 = get_closing_balance_debit(self.file, "41013")
        report_2 = get_closing_balance_debit(self.file, "41021")
        report_4 = get_closing_balance_debit(self.file, "41022")
        self.total_second = report_1 + report_2 + report_4

        return {
            "total": self.total_second,
            "report_1": report_1,
            "report_2": report_2,
            "report_4": report_4,
        }

    def nineth_report(self):
        report_2 = get_closing_balance_credit(self.file, "51028")
        self.total_nineth = report_2

        return {"total": self.total_nineth, "report_2": report_2}

    def tenth_report(self):
        report_1 = get_closing_balance_debit(self.file, "41018")
        self.total_tenth = report_1

        return {"total": self.total_tenth, "report_1": report_1}

    def fifteenth_report(self):
        report_2 = get_closing_balance_credit(self.file, "5109")
        report_3 = get_closing_balance_credit(
            self.file, "55062"
        ) + get_closing_balance_credit(self.file, "5508")
        report_4 = get_closing_balance_credit(self.file, "5704")
        self.total_fifteenth = report_2 + report_3 + report_4

        return {
            "total": self.total_fifteenth,
            "report_2": report_2,
            "report_3": report_3,
            "report_4": report_4,
        }

    def sixteenth_report(self):
        report_1 = get_closing_balance_debit(self.file, "420")
        report_2 = get_closing_balance_debit(self.file, "440")
        self.total_sixteenth = report_1 + report_2

        return {
            "total": self.total_sixteenth,
            "report_1": report_1,
            "report_2": report_2,
        }

    def seventeenth_report(self):
        report_1 = get_closing_balance_debit(self.file, "460")
        self.total_seventeenth = report_1

        return {"total": self.total_seventeenth, "report_1": report_1}

    def eigthteenth_report(self):
        report_1 = get_closing_balance_debit(self.file, "4109")
        report_2 = get_closing_balance_debit(self.file, "45062")
        report_3 = get_closing_balance_debit(self.file, "4704")
        self.total_eigthteenth = report_1 + report_2 + report_3

        return {
            "total": self.total_eigthteenth,
            "report_1": report_1,
            "report_2": report_2,
            "report_3": report_3,
        }

    def nineteenth_report(self):
        report_1 = get_closing_balance_debit(
            self.file, "47012"
        ) + get_closing_balance_debit(self.file, "4705")
        report_2 = get_closing_balance_credit(
            self.file, "57012"
        ) + get_closing_balance_credit(self.file, "5705")
        self.total_nineteenth = report_1 - report_2

        return {
            "total": self.total_nineteenth,
            "report_1": report_1,
            "report_2": report_2,
        }

    def twenty_first_report(self):
        report_1 = get_closing_balance_debit(self.file, "490")
        self.total_twenty_first = report_1

        return {"total": self.total_twenty_first, "report_1": report_1}
    
    def summarize(self):
        summary_1 = self.total_first - self.total_second
        summary_2 = summary_1 + self.total_nineth + self.total_tenth
        summary_3 = self.total_fifteenth + self.total_sixteenth + self.total_seventeenth + self.total_eigthteenth + self.total_nineteenth
        summary_4 = summary_2 - summary_3
        summary_5 = summary_4 - self.total_twenty_first

        return {
            "summary_1": summary_1,
            "summary_2": summary_2,
            "summary_3": summary_3,
            "summary_4": summary_4,
            "summary_5": summary_5,
        }
