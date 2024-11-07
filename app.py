import boto3
client = boto3.client('ec2')
response = client.run_instances(
   ImageId='ami-08ec94f928cf25a9d',
   InstanceType='t2.micro',
   KeyName='local',
   MaxCount=1,
   MinCount=1
)
