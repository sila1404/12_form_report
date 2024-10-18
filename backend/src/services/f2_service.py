import pandas as pd
from utils import get_closing_balance_debit


class F2:
    def __init__(self, file: pd.DataFrame) -> None:
        self.file = file

    def first_report(self) -> dict[str, int]:
        report_1 = get_closing_balance_debit(self.file, 1101)
        report_3 = get_closing_balance_debit(self.file, 112117)
        self.total_first = report_1 + report_3

        return {
            "total": self.total_first,
            "report_1": report_1,
            "report_3": report_3,
        }

    def second_report(self) -> dict[str, int]:
        report_1 = get_closing_balance_debit(
            self.file, 133111
        ) + get_closing_balance_debit(self.file, 113113)
        report_2 = get_closing_balance_debit(self.file, 113115)
        self.total_second = report_1 + report_2

        return {
            "total": self.total_second,
            "report_1": report_1,
            "report_2": report_2,
        }

    def fifth_report(self) -> dict[str, int]:
        report_1 = get_closing_balance_debit(self.file, 12031)
        report_2 = get_closing_balance_debit(self.file, 12831)
        report_4 = get_closing_balance_debit(self.file, 1299)
        self.total_fifth = report_1 + report_2 + report_4

        return {
            "total": self.total_fifth,
            "report_1": report_1,
            "report_2": report_2,
            "report_4": report_4,
        }

    def eighth_report(self) -> dict[str, int]:
        report_2 = get_closing_balance_debit(
            self.file, 1441
        ) - get_closing_balance_debit(self.file, 14821)
        report_3 = get_closing_balance_debit(
            self.file, 1442
        ) - get_closing_balance_debit(self.file, 14812)
        self.total_eighth = report_2 + report_3

        return {
            "total": self.total_eighth,
            "report_2": report_2,
            "report_3": report_3,
        }

    def tenth_report(self) -> dict[str, int]:
        report_1 = (
            get_closing_balance_debit(self.file, 12837)
            + get_closing_balance_debit(self.file, 12037)
            + get_closing_balance_debit(self.file, 1297)
        )
        report_3 = get_closing_balance_debit(
            self.file, 136137
        ) + get_closing_balance_debit(self.file, 138)
        self.total_tenth = report_1 + report_3

        return {
            "total": self.total_tenth,
            "report_1": report_1,
            "report_3": report_3,
        }

    def eleventh_report(self) -> dict[str, int]:
        report_3 = get_closing_balance_debit(self.file, 21323)
        self.total_eleventh = report_3

        return {
            "total": self.total_eleventh,
            "report_3": report_3,
        }

    def twelfth_report(self) -> dict[str, int]:
        report_1 = get_closing_balance_debit(self.file, 22013)
        report_2 = get_closing_balance_debit(self.file, 22015)
        self.total_twelfth = report_1 + report_2

        return {
            "total": self.total_twelfth,
            "report_1": report_1,
            "report_2": report_2,
        }

    def fifteenth_report(self) -> dict[str, int]:
        report_1 = (
            get_closing_balance_debit(self.file, 2137)
            + get_closing_balance_debit(self.file, 2207)
            + get_closing_balance_debit(self.file, 23883)
        )
        self.total_fifteenth = report_1

        return {
            "total": self.total_fifteenth,
            "report_1": report_1,
        }

    def sixteenth_report(self) -> dict[str, int]:
        report_1 = get_closing_balance_debit(self.file, 3101)
        report_3 = get_closing_balance_debit(self.file, 3202)
        report_4 = get_closing_balance_debit(self.file, 3203)
        report_5 = get_closing_balance_debit(
            self.file, 3204
        ) + get_closing_balance_debit(self.file, 3208)
        report_9 = get_closing_balance_debit(self.file, 3908)
        report_11 = get_closing_balance_debit(self.file, 3701)
        self.total_sixteenth = (
            report_1 + report_3 + report_4 + report_5 + report_9 + report_11
        )

        return {
            "total": self.total_sixteenth,
            "report_1": report_1,
            "report_3": report_3,
            "report_4": report_4,
            "report_5": report_5,
            "report_9": report_9,
            "report_11": report_11,
        }
