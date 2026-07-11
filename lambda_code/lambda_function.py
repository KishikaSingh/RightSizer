import json
from datetime import datetime

from Rightsizer.lambda_code.ec2_service import get_running_instances
from Rightsizer.lambda_code.cloudwatch_service import get_metrics
from Rightsizer.lambda_code.analyzer import analyze
from Rightsizer.lambda_code.report_generator import generate_report
from Rightsizer.lambda_code.s3_service import upload_report, upload_log
from Rightsizer.lambda_code.sns_service import send_notification


def lambda_handler(event, context):

    instances = get_running_instances()

    reports = []

    summary = {
        "UNDERUTILIZED": 0,
        "OPTIMAL": 0,
        "HIGH UTILIZATION": 0,
        "OVERUTILIZED": 0
    }

    for instance in instances:

        metrics = get_metrics(instance["InstanceId"])

        analysis = analyze(metrics)

        report = generate_report(instance, metrics, analysis)

        reports.append(report)

        summary[analysis["Status"]] += 1

    final_report = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "TotalInstances": len(instances),
        "Summary": summary,
        "Instances": reports
    }

    file_name = datetime.now().strftime("%Y%m%d_%H%M%S")

    upload_report(final_report, file_name)

    log = f"""
Execution Time : {datetime.now()}

Instances Scanned : {len(instances)}

Underutilized : {summary['UNDERUTILIZED']}

Optimal : {summary['OPTIMAL']}

High Utilization : {summary['HIGH UTILIZATION']}

Overutilized : {summary['OVERUTILIZED']}
"""

    upload_log(log, file_name)

    message = f"""
EC2 Rightsizing Analysis Completed

Total Instances : {len(instances)}

Underutilized : {summary['UNDERUTILIZED']}

Optimal : {summary['OPTIMAL']}

High Utilization : {summary['HIGH UTILIZATION']}

Overutilized : {summary['OVERUTILIZED']}

Detailed report has been uploaded to S3.
"""

    send_notification(message)

    return {
        "statusCode": 200,
        "body": json.dumps("Analysis Completed Successfully")
    }