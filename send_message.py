import boto3
import json
from credentials import *
curl = "https://sqs.us-east-2.amazonaws.com/440848399208/queue_29"

response = sqs.send_message(
    QueueUrl = curl, 
    MessageBody = "fesaiofsaefcasoiejf"
)

print(response)
