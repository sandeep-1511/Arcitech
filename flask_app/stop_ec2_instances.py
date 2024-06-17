import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # Filter EC2 instances by tag
    instances = ec2.describe_instances(Filters=[{'Name': 'tag:Environment', 'Values': ['Production']}])
    
    # Extract instance IDs
    instance_ids = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    
    # Stop the instances
    response = ec2.stop_instances(InstanceIds=instance_ids)
    print(response)
