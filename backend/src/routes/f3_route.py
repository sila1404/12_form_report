from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
import pandas as pd
from services import F3

f3_route = APIRouter(prefix="/reports")

@f3_route.get("/f3")
def get_f3_report(req: Request):
    """
    Retrieve the F3 report based on the uploaded DataFrame.

    Returns:
        JSON response containing the F3 report data.
    """
    df_report: pd.DataFrame = getattr(req.app.state, "df_report", None)

    # Check if the DataFrame exists
    if df_report is None:
        return JSONResponse(
            content={"error": "No report available. Please upload the file first."},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    # Generate the F3 report
    f3 = F3(df_report)
    first_report = f3.first_report()

    # Extracting totals and report values
    # total = first_report.get("total", 0)
    # report_1 = first_report.get("report_1", 0)
    # report_2 = first_report.get("report_2", 0)

    # Structuring the response data
    # response_data = {
    #     "index": [0, 1, 2],
    #     "columns": ["ລາຍການ", "ຈໍານວນເງິນ (ກີບ)"],
    #     "data": [
    #         ["1. ລາຍຮັບດອກເບ້ຍ ແລະ ທີ່ຖືຄືວ່າດອກເບ້ຍ", total],
    #         ["1.1 ລາຍຮັບຈາກການເຄື່ອນໄຫວລະຫວ່າງທະນາຄານ", report_1],
    #         ["1.2 ລາຍຮັບຈາກການເຄື່ນໄຫວຈາກລູກຄ້າ", report_2]
    #     ]
    # }

    return JSONResponse(content={"data": first_report}) 
