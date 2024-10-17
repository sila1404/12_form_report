from fastapi import APIRouter, Request
import pandas as pd
from services import F3


f3_route = APIRouter(prefix="/reports")


@f3_route.get("/f3")
def get_f3_report(req: Request):
    df_report: pd.DataFrame = req.app.state.df_report

    if df_report is None:
        return {"error": "No report available. Please upload the file first."}

    f3 = F3(df_report)

    return {"first_report": f3.first_report()}
