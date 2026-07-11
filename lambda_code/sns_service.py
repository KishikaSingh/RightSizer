import boto3
from Rightsizer.lambda_code.config import SNS_TOPIC_ARN

sns = boto3.client("sns")


def send_notification(
    total_instances,
    stop_instances,
    downsize_instances,
    keep_instances,
    investigate_instances,
    monthly_savings,
    annual_savings
):

    subject = "EC2 Rightsizer V2 Report"

    message = f"""
EC2 Rightsizer V2 Report

Total Instances Scanned : {total_instances}

Stop Idle Instances : {stop_instances}

Downsize Instances : {downsize_instances}

Keep Current Instances : {keep_instances}

Investigate High Utilization : {investigate_instances}

Estimated Monthly Savings : ${monthly_savings:.2f}

Estimated Annual Savings : ${annual_savings:.2f}

Detailed report has been uploaded to Amazon S3.
"""

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=subject,
        Message=message
    )