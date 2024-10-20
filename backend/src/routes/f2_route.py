from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
import pandas as pd
from services import F2

f2_route = APIRouter(prefix="/reports")


@f2_route.get("/f2")
async def get_first_f2_total(req: Request):
    df_report: pd.DataFrame = req.app.state.df_report
    if df_report is None:
        return JSONResponse(
            content={"error": "No report available. Please upload the file first"},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    f2 = F2(df_report)

    return JSONResponse(content={"first_report": f2.first_report()})
