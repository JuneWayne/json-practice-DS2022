import boto3
import json
from credentials import *

qurl = "https://sqs.us-east-2.amazonaws.com/440848399208/queue_29"

response = sqs.receive_message(
    QueueUrl = qurl,
)

print(response['Messages'][0]['Body'])