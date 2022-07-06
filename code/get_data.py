import json
import boto3

TABLE_NAME = "demotable"

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    if 'pathParameters' in event and event["pathParameters"]:
        results = dynamodb.get_item(TableName=TABLE_NAME, Key={'id':{'S':event["pathParameters"]["id"]}})
        return {
            'statusCode': 200,
            'body': json.dumps(results['Item'])
        }
    else:
        results = dynamodb.scan(
        TableName=TABLE_NAME,
        Limit=5,
        )
        return {
            'statusCode': 200,
            'body': json.dumps(results['Items'])
        }
