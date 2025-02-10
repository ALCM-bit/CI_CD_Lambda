import json

def lambda_handler(event, contex):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from lambda!')
    }