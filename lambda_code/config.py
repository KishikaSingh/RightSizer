import os

# AWS Resources

BUCKET_NAME = os.environ["BUCKET_NAME"]
SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]

# CloudWatch

METRIC_DURATION_DAYS = 7

# CPU Thresholds

STOP_THRESHOLD = 10
DOWNSIZE_THRESHOLD = 30
KEEP_THRESHOLD = 70

# EC2 Monthly Pricing (USD)

INSTANCE_PRICES = {

    "t2.micro": 8.50,
    "t2.small": 17.00,
    "t2.medium": 34.00,

    "t3.micro": 7.60,
    "t3.small": 15.20,
    "t3.medium": 30.40

}