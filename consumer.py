import json
import boto3
import datetime as dt


s3client = boto3.client('s3')
ssmclient = boto3.client('ssm')

def main(event, context):
    body = {
        "message": "Your function executed successfully!",
        "input": event,
    }

    try:

        action = event['detail']['action']
        state = event['detail']['state']
        keyname = timenow() + action + "_" + state

        bucketparam = get_ssm_bucketname("bucketname")

        print(bucketparam.get("Parameter").get("Value"))
  
        
        s3ClientResponse = s3client.put_object(
            Body=action + "_" + state,
            Bucket=bucketparam.get("Parameter").get("Value"),

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

def get_ssm_bucketname(parameter_name):
    return ssmclient.get_parameter(
        Name=parameter_name,
        WithDecryption=False
    )

if __name__ == '__main__':
    main('{}','{}')