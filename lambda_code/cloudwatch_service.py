import boto3
from datetime import datetime, timedelta
from Rightsizer.lambda_code.config import ANALYSIS_WINDOW_MINUTES, METRIC_PERIOD

cloudwatch = boto3.client("cloudwatch")


def get_metrics(instance_id):

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(minutes=ANALYSIS_WINDOW_MINUTES)

    response = cloudwatch.get_metric_data(

        MetricDataQueries=[

            {
                "Id": "cpu",
                "MetricStat": {
                    "Metric": {
                        "Namespace": "AWS/EC2",
                        "MetricName": "CPUUtilization",
                        "Dimensions": [
                            {
                                "Name": "InstanceId",
                                "Value": instance_id
                            }
                        ]
                    },
                    "Period": METRIC_PERIOD,
                    "Stat": "Average"
                }
            },

            {
                "Id": "networkin",
                "MetricStat": {
                    "Metric": {
                        "Namespace": "AWS/EC2",
                        "MetricName": "NetworkIn",
                        "Dimensions": [
                            {
                                "Name": "InstanceId",
                                "Value": instance_id
                            }
                        ]
                    },
                    "Period": METRIC_PERIOD,
                    "Stat": "Average"
                }
            },

            {
                "Id": "networkout",
                "MetricStat": {
                    "Metric": {
                        "Namespace": "AWS/EC2",
                        "MetricName": "NetworkOut",
                        "Dimensions": [
                            {
                                "Name": "InstanceId",
                                "Value": instance_id
                            }
                        ]
                    },
                    "Period": METRIC_PERIOD,
                    "Stat": "Average"
                }
            },

            {
                "Id": "memory",
                "MetricStat": {
                    "Metric": {
                        "Namespace": "CWAgent",
                        "MetricName": "mem_used_percent",
                        "Dimensions": [
                            {
                                "Name": "InstanceId",
                                "Value": instance_id
                            }
                        ]
                    },
                    "Period": METRIC_PERIOD,
                    "Stat": "Average"
                }
            },

            {
                "Id": "disk",
                "MetricStat": {
                    "Metric": {
                        "Namespace": "CWAgent",
                        "MetricName": "disk_used_percent",
                        "Dimensions": [
                            {
                                "Name": "InstanceId",
                                "Value": instance_id
                            }
                        ]
                    },
                    "Period": METRIC_PERIOD,
                    "Stat": "Average"
                }
            }

        ],

        StartTime=start_time,
        EndTime=end_time
    )

    metrics = {}

    for result in response["MetricDataResults"]:

        if result["Values"]:
            metrics[result["Id"]] = round(result["Values"][0], 2)
        else:
            metrics[result["Id"]] = 0

    return metrics