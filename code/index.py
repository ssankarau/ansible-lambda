import json
import boto3
dynamodb = boto3.client('dynamodb')
def lambda_handler(event, context):
    # TODO implement
    results = dynamodb.get_item(TableName='demotable', Key={'id':{'S':'1'}})
    return {
        'statusCode': 200,
        'body': json.dumps(results['Item'])
    }
