import boto3
import json
import os

bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    aws_access_key_id=os.getenv('aws_access_key_id'),
    aws_secret_access_key=os.getenv('aws_secret_access_key'),
    region_name='us-west-2'
)

prompt = "Create me a testing plan for a new generative AI product to be released to the public."

request_body = json.dumps({
    "inputText": prompt,
    "textGenerationConfig": {
        "maxTokenCount": 512,
        "temperature": 0.5,
    },
})

modelId = 'amazon.titan-text-express-v1'
accept = 'application/json'
contentType = 'application/json'
generatedText = "\n"

model_response = bedrock_runtime.invoke_model(body=request_body, modelId=modelId, accept=accept, contentType=contentType)
response_contents = json.loads(model_response.get('body').read())

generatedText = response_contents.get('results')[0].get('outputText')

print(generatedText)