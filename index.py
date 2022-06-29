import json
import boto3

def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])  

    #Sending message to our SQS 
    sqs = boto3.client('sqs')
    sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/790101844276/Karmel-Queue",
        MessageBody=message
    )

    #Return message
    return { 
        'message' : message
    }
