from Rightsizer.lambda_code.ec2_service import get_running_instances
from Rightsizer.lambda_code.cloudwatch_service import get_instance_metrics
from Rightsizer.lambda_code.recommendation_engine import get_recommendation
from Rightsizer.lambda_code.cost_analyser import calculate_savings
from Rightsizer.lambda_code.report_generator import generate_report
from Rightsizer.lambda_code.s3_service import upload_report
from Rightsizer.lambda_code.sns_service import send_notification


def lambda_handler(event, context):

    instances = get_running_instances()

    reports = []

    total_monthly_savings = 0
    total_annual_savings = 0

    stop_instances = 0
    downsize_instances = 0
    keep_instances = 0
    investigate_instances = 0

    for instance in instances:

        metrics = get_instance_metrics(instance["InstanceId"])

        recommendation = get_recommendation(metrics)

        savings = calculate_savings(
            instance["InstanceType"],
            recommendation
        )

        report = generate_report(
            instance,
            metrics,
            recommendation,
            savings
        )

        reports.append(report)

        total_monthly_savings += savings["MonthlySaving"]
        total_annual_savings += savings["AnnualSaving"]

        if recommendation == "Stop Idle Instance":
            stop_instances += 1

        elif recommendation == "Downsize Instance":
            downsize_instances += 1

        elif recommendation == "Keep Current Instance":
            keep_instances += 1

        else:
            investigate_instances += 1

    upload_report(reports)

    send_notification(
        total_instances=len(instances),
        stop_instances=stop_instances,
        downsize_instances=downsize_instances,
        keep_instances=keep_instances,
        investigate_instances=investigate_instances,
        monthly_savings=total_monthly_savings,
        annual_savings=total_annual_savings
    )

    return {
        "statusCode": 200,
        "body": "EC2 Rightsizing Analysis Completed Successfully"
    }