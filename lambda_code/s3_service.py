import boto3
import json
from datetime import datetime
from Rightsizer.lambda_code.config import BUCKET_NAME

s3 = boto3.client("s3")


def upload_report(report):

    file_name = f"reports/report_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=json.dumps(report, indent=4),
        ContentType="application/json"
    )

    return file_name