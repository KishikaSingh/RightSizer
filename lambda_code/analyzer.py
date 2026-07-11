from Rightsizer.lambda_code.config import METRIC_WEIGHTS, UTILIZATION_POLICY, RECOMMENDATIONS


def analyze(metrics):

    cpu = metrics["cpu"]
    memory = metrics["memory"]
    disk = metrics["disk"]

    overall_score = (
        cpu * METRIC_WEIGHTS["cpu"] +
        memory * METRIC_WEIGHTS["memory"] +
        disk * METRIC_WEIGHTS["disk"]
    )
    

    overall_score = round(overall_score, 2)

    # Determine Status
    if overall_score < UTILIZATION_POLICY["UNDERUTILIZED"][1]:

        status = "UNDERUTILIZED"

    elif overall_score < UTILIZATION_POLICY["OPTIMAL"][1]:

        status = "OPTIMAL"

    elif overall_score < UTILIZATION_POLICY["HIGH_UTILIZATION"][1]:

        status = "HIGH UTILIZATION"

    else:

        status = "OVERUTILIZED"

    return {
        "OverallScore": overall_score,
        "Status": status,
        "Recommendation": RECOMMENDATIONS[status]
    }