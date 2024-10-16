from fastapi import APIRouter, Request
import pandas as pd
from services import F2

f2_route = APIRouter(prefix="/reports")


@f2_route.get("/f2")
async def get_first_f2_total(req: Request):
    df_report: pd.DataFrame = req.app.state.df_report
    if df_report is None:
        return {"error": "No report available. Please upload the file first"}

    f2 = F2(df_report)

    return {"first_report": f2.first_report()}


