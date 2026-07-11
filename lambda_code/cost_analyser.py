from Rightsizer.lambda_code.pricing import get_instance_price


def calculate_savings(instance_type, recommendation):

    current_price = get_instance_price(instance_type)

    monthly_saving = 0

    if recommendation == "Stop Idle Instance":

        monthly_saving = current_price

    elif recommendation == "Downsize Instance":

        monthly_saving = current_price * 0.50

    annual_saving = monthly_saving * 12

    return {

        "MonthlySaving": round(monthly_saving, 2),

        "AnnualSaving": round(annual_saving, 2)

    }