from datetime import datetime


def generate_report(instance, metrics, analysis):

    report = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "InstanceId": instance["InstanceId"],

        "InstanceType": instance["InstanceType"],

        "Metrics": {
            "CPUUtilization": metrics["cpu"],
            "MemoryUtilization": metrics["memory"],
            "DiskUtilization": metrics["disk"],
            "NetworkIn": metrics["networkin"],
            "NetworkOut": metrics["networkout"]
        },

        "OverallScore": analysis["OverallScore"],

        "Status": analysis["Status"],

        "Recommendation": analysis["Recommendation"]
    }

    return report