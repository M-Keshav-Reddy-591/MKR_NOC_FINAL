from fastapi import APIRouter, UploadFile, File
import pandas as pd

router = APIRouter(
    prefix="/api/v1/roster",
    tags=["Roster Upload"]
)

@router.post("/upload")

async def upload_roster(
    file: UploadFile = File(...)
):

    df = pd.read_csv(file.file)

    data = df.to_dict(orient="records")

    return {
        "message": "Roster uploaded successfully",
        "data": data
    }