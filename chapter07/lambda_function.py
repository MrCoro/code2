
import boto3
ec2 = boto3.client('ec2')
def lambda_handler(event, context):

  eventName = event['detail']['eventName']

  if eventName == 'RunInstances':
    userName = event['detail']['userIdentity']['arn'].split('/')[1]
    instanceId = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']    
    print("Adding owner tag " + userName + " to instance " + instanceId + ".")
    try:
      ec2.create_tags(Resources=[instanceId,],Tags=[{'Key': 'Owner', 'Value': userName},])
      return
    except Exception as e:
      print(e)
      raise e
  else:
    return
