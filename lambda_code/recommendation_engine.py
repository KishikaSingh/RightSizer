from Rightsizer.lambda_code.config import STOP_THRESHOLD, DOWNSIZE_THRESHOLD, KEEP_THRESHOLD


def get_recommendation(metrics):

    cpu = metrics["CPU"]

    if cpu < STOP_THRESHOLD:
        return "Stop Idle Instance"

    elif cpu < DOWNSIZE_THRESHOLD:
        return "Downsize Instance"

    elif cpu < KEEP_THRESHOLD:
        return "Keep Current Instance"

    else:
        return "Investigate High Utilization"