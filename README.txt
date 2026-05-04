AWS Image Label Detector
Author: Navneet Sinha
Date: 23/04/2026

Files in this ZIP:

1. lambda_function.py
   The Python code deployed as an AWS Lambda function. 
   Connects to Amazon Rekognition to detect image labels.

2. index.html
   The frontend web page hosted on Amazon S3. 
   Uploads images to S3 and calls the API Gateway endpoint.

3. screenshots/
   - lambda.png        — Lambda function in AWS Console
   - api-gateway.png   — API Gateway REST API configuration
   - s3-buckets.png    — Two S3 buckets (frontend + image storage)
   - app-working.png   — Working web app with detected labels

AWS Architecture: See architecture diagram in the accompanying PDF report.

The link for the working website is:-
http://rekognition-frontend-navneet.s3-website-us-east-1.amazonaws.com