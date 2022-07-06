import json
import boto3

TABLE_NAME = "demotable"

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    input_body = json.loads(event['body'])
    try:
        table.update_item(
            Key={
                    'id': input_body["id"],
                },
            UpdateExpression="set fname = :n",
            ExpressionAttributeValues={
                    ':n': input_body["fname"]
                },
            ReturnValues="UPDATED_NEW"
            )
        
        return {
            'statusCode': 200,
            'body': json.dumps({ "id" : input_body["id"], "message": "inserted successfully" })
        }
    except:
        return {
            'statusCode': 500,
            'body': json.dumps({ "id" : input_body["id"], "message": "Something Went Wrong" })
        }
