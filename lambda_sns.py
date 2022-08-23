import json
import boto3

s3 = boto3.resource('s3')
sns = boto3.client('sns')

def lambda_handler(event,context):
     
    bkt = s3.Bucket('test9959')
    count =0
    for obj in bkt.objects.all():
        count+=1
        print(obj.key)
    print(count)
    if count != 0:
        print('Object found. Sending notification')
        sns.publish(TopicArn='arn:aws:sns:us-east-1:405259030962:notif',Message='The file is uploaded. The number of submissions received are ' + str(count) , Subject='Submission received')
    else:
        print('File was not present')