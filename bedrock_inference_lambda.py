import boto3
import json

def lambda_handler(event, context):
    # Expect the event to contain a validated 'prompt'
    prompt = event.get('prompt', "create me a testing plan for a new generative AI product to be released to the public.")
    
    bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-west-2')
    
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
    
    try:
        model_response = bedrock_runtime.invoke_model(
            body=request_body,
            modelId=modelId,
            accept=accept,
            contentType=contentType
        )
        response_contents = json.loads(model_response.get('body').read())
        generatedText = response_contents.get('results')[0].get('outputText')
    except Exception as e:
        return {
            "error": str(e)
        }
    
    return {
        "prompt": prompt,
        "generatedText": generatedText
    }
