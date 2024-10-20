from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
import pandas as pd
from services import F3


f3_route = APIRouter(prefix="/reports")


@f3_route.get("/f3")
def get_f3_report(req: Request):
    df_report: pd.DataFrame = getattr(req.app.state, "df_report", None)

    if df_report is None:
        return JSONResponse(
            content={"error": "No report available. Please upload the file first."},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    f3 = F3(df_report)

    return JSONResponse(content={"first_report": f3.first_report()})
