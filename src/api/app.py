from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from s3.s3_uploader import upload_file_to_s3
from utils.logger import get_logger
from .env import S_BucketName

app = FastAPI()
logger = get_logger("Running FastAPI Script")

BUCKET_NAME = S_BucketName

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    try:
        file_content = await file.read()
        file_obj = file.file
        object_name = file.filename

        file.file.seek(0)

        success = upload_file_to_s3(file_obj, BUCKET_NAME, object_name)

        if success:
            return JSONResponse(status_code=200, content={"message": "File uploaded successfully"})
        else:
            raise HTTPException(status_code=500, detail="Upload to S3 failed")
        
    except Exception as e:
        logger.error(f"Upload Failed: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")