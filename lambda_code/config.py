"""
===========================================================
Configuration File
EC2 Rightsizing & Cost Optimization Analyzer
===========================================================
"""

import os

# ==========================================================
# AWS Resources
# ==========================================================

# S3 Bucket to store reports and logs
BUCKET_NAME = os.environ.get(
    "BUCKET_NAME",
    "costoptima-reports-kishika"
)

# SNS Topic ARN for notifications
SNS_TOPIC_ARN = os.environ.get(
    "SNS_TOPIC_ARN",
    "arn:aws:sns:ap-south-1:546854094255:costOptima_notification"
)

# ==========================================================
# CloudWatch Configuration
# ==========================================================

# Analyze the previous 5 minutes
ANALYSIS_WINDOW_MINUTES = 5

# CloudWatch metric period (300 sec = 5 min)
METRIC_PERIOD = 300

# ==========================================================
# Metric Weights
# (Must total 1.0)
# ==========================================================

METRIC_WEIGHTS = {
    "cpu": 0.40,
    "memory": 0.35,
    "disk": 0.25
}

# ==========================================================
# Utilization Policy
# ==========================================================

UTILIZATION_POLICY = {
    "UNDERUTILIZED": (0, 25),
    "OPTIMAL": (25, 70),
    "HIGH_UTILIZATION": (70, 85),
    "OVERUTILIZED": (85, 100)
}

# ==========================================================
# Recommendation Mapping
# ==========================================================

RECOMMENDATIONS = {
    "UNDERUTILIZED": "Rightsize or Stop Instance",
    "OPTIMAL": "No Action Required",
    "HIGH_UTILIZATION": "Monitor Workload",
    "OVERUTILIZED": "Upgrade Instance"
}

# ==========================================================
# CloudWatch Metrics
# ==========================================================

METRICS = {

    "cpu": {
        "namespace": "AWS/EC2",
        "metric": "CPUUtilization",
        "stat": "Average"
    },

    "memory": {
        "namespace": "CWAgent",
        "metric": "mem_used_percent",
        "stat": "Average"
    },

    "disk": {
        "namespace": "CWAgent",
        "metric": "disk_used_percent",
        "stat": "Average"
    },

    "network_in": {
        "namespace": "AWS/EC2",
        "metric": "NetworkIn",
        "stat": "Average"
    },

    "network_out": {
        "namespace": "AWS/EC2",
        "metric": "NetworkOut",
        "stat": "Average"
    }

}

# ==========================================================
# S3 Folder Structure
# ==========================================================

REPORT_FOLDER = "reports/"
LOG_FOLDER = "logs/"