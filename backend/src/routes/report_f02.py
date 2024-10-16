from fastapi import APIRouter, Request
from services import F02

f02_route = APIRouter(prefix="/reports/f02")

report_f02 = None


@f02_route.get("/1")
async def get_first_f02_total(req: Request):
    report: dict[str, any] = req.app.state.report
    if report is None:
        return {"error": "No report available. Please upload the file first"}

    f02 = F02(report)

    return f02.file


# @f02_route.get("/test")
# def test(req: Request):
#     state = req.app.state.report
#     print(state)
#     return "Hello world"
