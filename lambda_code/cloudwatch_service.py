import boto3
from datetime import datetime, timedelta
from Rightsizer.lambda_code.config import METRIC_DURATION_DAYS

cloudwatch = boto3.client("cloudwatch")


def get_average_metric(namespace, metric_name, instance_id):

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=METRIC_DURATION_DAYS)

    response = cloudwatch.get_metric_statistics(
        Namespace=namespace,
        MetricName=metric_name,

        Dimensions=[
            {
                "Name": "InstanceId",
                "Value": instance_id
            }
        ],

        StartTime=start_time,
        EndTime=end_time,

        Period=3600,
        Statistics=["Average"]
    )

    datapoints = response["Datapoints"]

    if not datapoints:
        return 0

    total = 0

    for point in datapoints:
        total += point["Average"]

    return round(total / len(datapoints), 2)


def get_instance_metrics(instance_id):

    metrics = {

        "CPU": get_average_metric(
            "AWS/EC2",
            "CPUUtilization",
            instance_id
        ),

        "Memory": get_average_metric(
            "CWAgent",
            "mem_used_percent",
            instance_id
        ),

        "Disk": get_average_metric(
            "CWAgent",
            "disk_used_percent",
            instance_id
        )

    }

    return metrics
    