from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Split
import pandas as pd
from services import F3

# Define the model
class AccountCodeReport(BaseModel):
    account_code: int
    balance: int

class F3ReportSection(BaseModel):
    total: int
    report_1: int
    report_2: Optional[int] = None
    additional_reports: Optional[List[AccountCodeReport]] = None

class F3Report(BaseModel):
    first_report: F3ReportSection
    second_report: Optional[F3ReportSection] = None

# Create the route
f3_route = APIRouter(prefix="/reports")

@f3_route.get("/f3", response_model=F3Report)
def get_f3_report(req: Request):
    df_report: pd.DataFrame = getattr(req.app.state, "df_report", None)

    if df_report is None:
        return JSONResponse(
            content={"error": "No report available. Please upload the file first."},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    f3 = F3(df_report)

    first_report = f3.first_report()
    second_report = f3.second_report()

