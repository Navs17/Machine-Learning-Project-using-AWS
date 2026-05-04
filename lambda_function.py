import json
import boto3

rekognition = boto3.client('rekognition')
BUCKET_NAME = 'rekognition-images-navneet'

def lambda_handler(event, context):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,POST'
    }
    
    if event.get('httpMethod') == 'OPTIONS':
        return {'statusCode': 200, 'headers': headers, 'body': ''}
    
    try:
        body = json.loads(event['body'])
        image_key = body['imageKey']
        
        response = rekognition.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': BUCKET_NAME,
                    'Name': image_key
                }
            },
            MaxLabels=10,
            MinConfidence=70
        )
        
        labels = [
            {'name': label['Name'], 'confidence': round(label['Confidence'], 2)}
            for label in response['Labels']
        ]
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'labels': labels})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }