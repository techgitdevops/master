import boto3
client = boto3.client('rds')
response = client.run_instances(
   ImageId='ami-08ec94f928cf25a9d',
   InstanceType='t2.micro',
   KeyName='frankfurtkey',
   MaxCount=1,
   MinCount=1
)
