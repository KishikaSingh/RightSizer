from Rightsizer.lambda_code.config import INSTANCE_PRICES


def get_instance_price(instance_type):

    return INSTANCE_PRICES.get(instance_type, 0)