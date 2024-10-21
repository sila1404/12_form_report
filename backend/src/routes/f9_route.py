from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
import pandas as pd


f9_route = APIRouter(prefix="/reports")


@f9_route.get("/f9")
def get_f3_report(req: Request):
    df_report: pd.DataFrame = getattr(req.app.state, "df_report", None)

    if df_report is None:
        return JSONResponse(
            content={"error": "No report available. Please upload the file first."},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return JSONResponse(content=df_report.to_dict(orient="split"))