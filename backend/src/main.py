from fastapi import FastAPI, File, UploadFile
from io import BytesIO

from utils import read_file
from routes import f2_route

app = FastAPI()

app.state.report = None


@app.post("/upload")
async def upload(file: UploadFile = File(None)):
    # If no file and no existing report, return an error
    if file is None:
        return {"error": "No file uploaded and no existing report."}

    # If the file is provided, update the report
    if file.filename.endswith((".xlsx", ".xls")):
        try:
            contents = await file.read()
            df = read_file(BytesIO(contents))
            # Store the report dataframe in app state to use it across the project
            app.state.df_report = df
            return {"message": "File uploaded successfully"}
        except Exception as e:
            return {"error": f"An error occur while processing the file: {e}"}
    else:
        return {"error": "Invalid file type. Please upload an Excel file"}


@app.get("/")
def root():
    return {"message": "Hello, World!"}


app.include_router(f2_route)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
