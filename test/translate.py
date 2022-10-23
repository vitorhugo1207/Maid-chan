import requests
import json
        # anilistPOST = str(anilistPOST.text)
        # anilistPOST = json.loads(str(anilistPOST))

def translate(inputTrans):
    
        url = f"https://translation.googleapis.com/language/translate/v2?key=???????????????????"
        inputTransObj = {
            "q": inputTrans,
            "target": "pt",
            "format": "text"
        }
        
        # outputTrans = requests.post(url, json=inputTransObj).text
        # outputTrans = requests.post(url, json=inputTransObj)
        # outputTrans = str(outputTrans.text)
        # outputTrans = json.loads(str(outputTrans))
        # print(outputTrans['data']['translations'][0]['detectedSourceLanguage'])


        langueTarget = inputTrans[+2:]
        print(langueTarget)

translate(inputTrans = "pt Hello, World!")
