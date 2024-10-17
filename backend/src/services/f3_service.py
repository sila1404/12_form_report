import pandas as pd
from utils import get_closing_balance_credit , get_closing_balance_debit





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
        self.total_first = report_1 + report_2

        return {"total": self.total_first, "report_1": report_1, "report_2": report_2}
    
    def second_report(self): 
        report_1 = get_closing_balance_debit(self.file, 41013)
        report_2 = get_closing_balance_debit(self.file, 41021)
        report_4 = get_closing_balance_debit(self.file, 41022)
        self.total_second = report_1 + report_2 + report_4
        return {
            "total":self.total_second,
            "report_1": report_1,
            "report_2": report_2,
            "report_4": report_4,
        }
    def nine_report(self):
        report_2 = get_closing_balance_credit(self.file, 51028)
        self.total_nine = report_2
        return {"total" : self.total_nine, "report_2": report_2}
       

    def ten_report(self):
        report_1 = get_closing_balance_debit(self.file, 41018)
        self.total_ten = report_1
        return {"total": self.total_ten, "report_1": report_1}
    def fifteen_report(self):
        report_2 = get_closing_balance_credit(self.file, 5109)
        report_3 = get_closing_balance_credit(self.file, 55062)
        + get_closing_balance_credit(self.file, 5508)
        report_4 = get_closing_balance_credit(self.file, 5704)
        self.total_fifteen = report_2 + report_3 + report_4
        return {
                "total": self.total_fifteen, 
                "report_2": report_2,
                "report_3": report_3,
                "report_4": report_4,
            }
    def sixteen_report(self):
        report_1 = get_closing_balance_debit(self.file, 420)
        report_2 = get_closing_balance_debit(self.file, 440)
        self.total_sixteen = report_1 + report_2
        return {
            "total": self.total_sixteen,
            "report_1": report_1,
            "report_2": report_2,
        }
    def seventeen_report(self):
        report_1 = get_closing_balance_debit(self.file, 460)
        self.total_seventeen = report_1
        return {"total": self.total_seventeen, "report_1": report_1}
    def eigthteen_report(self):
        report_1 = get_closing_balance_debit(self.file, 4109)
        report_2 = get_closing_balance_debit(self.file, 45062)
        report_3 = get_closing_balance_debit(self.file, 4704)
        self.total_eigthteen = report_1 + report_2 + report_3
        return {
            "total": self.total_eigthteen,
            "report_1": report_1,
            "report_2": report_2,
            "report_3": report_3,
        }
    def nineteen_report(self):
        report_1 = get_closing_balance_debit(self.file, 47012) + get_closing_balance_debit(self.file, 4705)
        report_2 = get_closing_balance_credit(self.file, 57012) + get_closing_balance_credit(self.file, 5705)
        self.total_nineteen = report_1 + report_2
        return {
            "total": self.total_nineteen,
            "report_1": report_1,
            "report_2": report_2,
        }
    def twenty_one_report(self):
        report_1 = get_closing_balance_debit(self.file , 490)
        self.total_twenty_one = report_1
        return {"total": self.total_twenty_one, "report_1": report_1}






      
