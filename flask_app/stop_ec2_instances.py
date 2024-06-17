import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # Filter instances by a specific tag
    response = ec2.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': ['YourInstanceTag']}])
    
    # Extract instance IDs
    instance_ids = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    
    # Stop instances
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Instances {instance_ids} stopped successfully")
    else:
        print("No instances found with the specified tag.")
