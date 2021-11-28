import json
import boto3
import datetime as dt


client = boto3.client('events')

def main(event, context):

    response = client.put_events(
        Entries=[
            {
                "Source": "producer",
                "DetailType": "web action",
                "Detail": "{\"action\": \"AddToBasket\", \"state\": \"Success\"}",
                "EventBusName": "default"
            },
        ]
    )

if __name__ == '__main__':
    main('{}','{}')
