import json
import boto3
import datetime as dt


client = boto3.client('s3')

def main(event, context):
    body = {
        "message": "Your function executed successfully!",
        "input": event,
    }

    try:

        instancename = event['detail']['instance-id']
        instancestate = event['detail']['state']
        keyname = timenow() + instancename + "_" + instancestate
        
        s3ClientResponse = client.put_object(
            Body=instancename + "_" + instancestate,
            Bucket="servlessbucket20211125b",

            Key=keyname,
        )

        print(s3ClientResponse)

    except Exception as ex:

        print(ex)
        

    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
    
def timenow():

    dateTimeObj = dt.datetime.now()
    date = dateTimeObj.strftime("%d-%b-%Y_%H-%M-%S_")
    
    return date

if __name__ == '__main__':
    main('{}','{}')