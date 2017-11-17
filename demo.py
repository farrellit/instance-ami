import boto3, json

def pull_instances(ec2):
    paginator = ec2.get_paginator('describe_instances')
    page = paginator.paginate()
    for resp in page:
      for reserv in resp['Reservations']:
        for instance in reserv['Instances']:
          yield instance

region_ami_instances = dict()
for region in boto3.session.Session().get_available_regions("ec2"):
  if region not in region_ami_instances.keys():
    region_ami_instances[region] = dict()
  ec2 = boto3.client("ec2", region_name=region)
  for instance in pull_instances(ec2):
    ami = instance['ImageId']
    if ami not in region_ami_instances[region].keys():
      region_ami_instances[region][ami] = list()
    region_ami_instances[region][ami].append( instance['InstanceId'] )

print(json.dumps(region_ami_instances, indent=2))
