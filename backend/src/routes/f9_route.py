from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
import pandas as pd
from utils import response_message

f9_route = APIRouter(prefix="/reports")


@f9_route.get("/f9")
def get_f3_report(req: Request):
    df_report: pd.DataFrame = getattr(req.app.state, "df_report", None)

    if df_report is None:
        return JSONResponse(
            content=response_message(
                message="No report available. Please upload the file first.",
                success=False,
            ),
            status_code=status.HTTP_404_NOT_FOUND,
        )
    
    try:
        return JSONResponse(
            content=response_message(
                message="Successfully load the F9 report data.",
                response_data=df_report.to_dict(orient="split"),
                success=True,
            )
        )
    
    except Exception as e:
        return JSONResponse(
            content=response_message(
                message=f"An internal error occurred: {e}", success=False
            ),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
