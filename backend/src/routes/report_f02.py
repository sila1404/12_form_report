from fastapi import APIRouter, Request
import pandas as pd
from services import F02

f02_route = APIRouter(prefix="/reports")


@f02_route.get("/f02")
async def get_first_f02_total(req: Request):
    df_report: pd.DataFrame = req.app.state.df_report
    if df_report is None:
        return {"error": "No report available. Please upload the file first"}

    f02 = F02(df_report)

    return {"first_report": f02.first_report()}


