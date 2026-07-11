import boto3
from Rightsizer.lambda_code.config import SNS_TOPIC_ARN

sns = boto3.client("sns")


def send_notification(message):

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="EC2 Rightsizing Report",
        Message=message
    )