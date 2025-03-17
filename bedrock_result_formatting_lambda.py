import json

def lambda_handler(event, context):
    generatedText = event.get("generatedText", "")
    prompt = event.get("prompt", "No prompt provided")
    
    formattedResult = {
        "prompt": prompt,
        "result": generatedText,
        "message": "Inference completed successfully."
    }
    
    return formattedResult
