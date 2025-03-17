import json

def lambda_handler(event, context):
    data = event.get('data', {})
    prompt = data.get('prompt')
    
    if not prompt:
        return {
            "isValid": False,
            "error": "Missing 'prompt' in input data."
        }
    
    return {
        "isValid": True,
        "prompt": prompt,
        "userId": data.get('userId', 'unknown')
    }
