#python -m pip install requests

import requests

API_KEY = "0bffabab-8341-453a-a518-3808f64987b8:fx"
BASE_URL = "https://api-free.deepl.com/v2/translate"

print ("Welcome")
print ("Enter text:")
print ("Text 'exit' to leave")

while True:
    translate = input("Enter text you want to translate")
    if translate.lower() == 'exit':
        print ("bye")
        break

    data = {
        "auth_key": API_KEY,
        "text": translate,
        "target_lang": "UK"
    }

    response = requests.post(BASE_URL, data=data)
    result = response.json()

    if "translations" in result:
        translated_text = result["translations"][0]["text"]
        print (f"Переклад: {translated_text}")