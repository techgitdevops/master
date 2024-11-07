import boto3
client = boto3.client('ec2')
response = client.run_instances(
   ImageId='ami-08ec94f928cf25a9d',
   InstanceType='t2.micro',
   KeyName='remote',
>>>>>>> 7db8a4715bd960079e382b288a46126d632146c1
   MaxCount=1,
   MinCount=1
)
