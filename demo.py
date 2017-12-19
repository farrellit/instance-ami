import boto3, json

def pull_instances(ec2):
    paginator = ec2.get_paginator('describe_instances')
    page = paginator.paginate()
    for resp in page:
      for reserv in resp['Reservations']:
        for instance in reserv['Instances']:
          yield instance

def pull_amis(ec2, images):
  args = dict(ImageIds=images)
  print(args)
  resp = ec2.describe_images(**args)
  for image in resp['Images']:
    yield image 

''' # I thought this was missing - but it turns out there just weren't tags in my test 
def pull_tags(ec2,resources):
  token = False
  args = dict(Filters=[{"Name":"resource-id","Values":resources}] )
  while token != None:
    if token:
      args['NextToken']=token
    res = ec2.describe_tags(**args)
    token = res.get('NextToken',None) 
    for tag in res['Tags']:
      yield tag
'''
region_ami_instances = dict()
for region in boto3.session.Session().get_available_regions("ec2"):
  #if region not in [ 'ca-central-1']: continue
  if region not in region_ami_instances.keys():
    region_ami_instances[region] = dict()
  ec2 = boto3.client("ec2", region_name=region)
  for instance in pull_instances(ec2):
    ami = instance['ImageId']
    if ami not in region_ami_instances[region].keys():
      region_ami_instances[region][ami] = { "instances":[] }
    region_ami_instances[region][ami]["instances"].append( instance['InstanceId'] )
  if len(region_ami_instances[region].keys()) == 0:
    continue
  for image in pull_amis(ec2, list(region_ami_instances[region].keys()) ):
    region_ami_instances[region][image['ImageId']]['image'] = image
"""
  for tag in pull_tags(ec2, list(region_ami_instances[region].keys()) ):
    image = tag['ResourceId']
    if 'Tags' not in region_ami_instances[region][image]['image'].keys():
      region_ami_instances[region][image]['image']['Tags'] = {}
    else:
    region_ami_instances[region][image]['image']['Tags'][tag['Key']] = tag['Value']
"""

print(json.dumps(region_ami_instances, indent=2))
