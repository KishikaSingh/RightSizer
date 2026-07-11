from datetime import datetime


def generate_report(instance, metrics, recommendation, savings):

    report = {

        "AnalysisTime": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),

        "InstanceId": instance["InstanceId"],

        "InstanceName": instance["InstanceName"],

        "InstanceType": instance["InstanceType"],

        "AvailabilityZone": instance["AvailabilityZone"],

        "Metrics": metrics,

        "Recommendation": recommendation,

        "MonthlySaving": savings["MonthlySaving"],

        "AnnualSaving": savings["AnnualSaving"]

    }

    return report