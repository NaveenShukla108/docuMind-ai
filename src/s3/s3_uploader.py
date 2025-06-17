import boto3
from botocore.exceptions import BotoCoreError, NoCredentialsError
from utils.logger import get_logger

logger = get_logger("S3-Uploader")

s3 = boto3.client("s3")

def upload_file_to_s3(file_obj, bucket_name, object_name):

    try:
        s3.upload_fileobj(file_obj, bucket_name, object_name)
        logger.info(f"File Uploaded to S3: s3://{bucket_name}/{object_name}")
        return True
    
    except (BotoCoreError, NoCredentialsError) as e:
        logger.error(f"S3 Upload Failed {e}")
        return False
    