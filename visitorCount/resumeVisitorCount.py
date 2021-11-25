import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("appData")

def get_count():
    resp = table.get_item(
    Key={
        'id':'resumechallengevisitors'
    }
)
    return int(resp['Item']['count'])

def lambda_handler(event, context):
    old_count = get_count()
    print("old count was "+str(old_count))
    new_count = old_count + 1
    print("new count is "+str(new_count))

    table.put_item(
       Item={
            'id':'resumechallengevisitors',
            'count': new_count
        }
    )
    
    return {  
        'statusCode': 200,
        'headers' : {
            "Access-Control-Allow-Origin" : "*"
    },
        'body': json.dumps(new_count)
    }