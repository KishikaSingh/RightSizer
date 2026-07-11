import boto3
import json
from Rightsizer.lambda_code.config import BUCKET_NAME

s3 = boto3.client("s3")


def upload_report(report, file_name):

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f"reports/{file_name}.json",
        Body=json.dumps(report, indent=4),
        ContentType="application/json"
    )


def upload_log(log_data, file_name):

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f"logs/{file_name}.txt",
        Body=log_data
    )