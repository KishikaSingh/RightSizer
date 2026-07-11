import boto3

ec2 = boto3.client("ec2")


def get_running_instances():

    response = ec2.describe_instances()

    instances = []

    for reservation in response["Reservations"]:

        for instance in reservation["Instances"]:

            if instance["State"]["Name"] != "running":
                continue

            name = "No Name"

            if "Tags" in instance:

                for tag in instance["Tags"]:

                    if tag["Key"] == "Name":
                        name = tag["Value"]

            instances.append({

                "InstanceId": instance["InstanceId"],

                "InstanceType": instance["InstanceType"],

                "InstanceName": name,

                "AvailabilityZone":
                instance["Placement"]["AvailabilityZone"]

            })

    return instances