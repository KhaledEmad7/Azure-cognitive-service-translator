import requests, uuid, json

# Add your subscription key and endpoint
subscription_key = "Your_subscription_key"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your region, also known as location. The default is global.
# This is required if using a Cognitive Services resource.
region = "Yout_region(ex: eastus)"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    #you can choose any languages here
    #here is the list: https://docs.microsoft.com/en-us/azure/cognitive-services/translator/language-support
    'from': 'en',
    'to': ['ar', 'de', 'fr']
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': region,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
text = input("Enter the text you want to translate:\n")
body = [{
    'text': text
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
