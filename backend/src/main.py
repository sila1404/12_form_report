from fastapi import FastAPI, File, UploadFile, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO

from utils import read_file
from routes import f2_route, f3_route, f9_route

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.state.report = None


@app.post("/upload")
async def upload(file: UploadFile = File(None)):
    # If no file and no existing report, return an error
    if file is None:
        return JSONResponse(
            content={"error": "No file uploaded and no existing report."},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    # If the file is provided, update the report
    if file.filename.endswith((".xlsx", ".xls")):
        try:
            contents = await file.read()
            df = read_file(BytesIO(contents))
            # Store the report dataframe in app state to use it across the project
            app.state.df_report = df.astype(object)
            return JSONResponse(content={"message": "File uploaded successfully"})
        except Exception as e:
            return JSONResponse(
                content={"error": f"An error occur while processing the file: {e}"},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    else:
        return JSONResponse(
            content={"error": "Invalid file type. Please upload an Excel file"},
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@app.get("/")
def root():
    return {"message": "Hello, World!"}


app.include_router(f2_route)
app.include_router(f3_route)
app.include_router(f9_route)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
