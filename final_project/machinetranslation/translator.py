"Provide methods for translation"
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishtofrench(englishtext):
    "Convert English to French"
    translation=''
    if englishtext is None or englishtext=='':
        return translation
    translation = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()
    frenchtext=translation['translations'][0]['translation']
    #print(json.dumps(translation, indent=2, ensure_ascii=False))

    return frenchtext

def frenchtoenglish(frenchtext):
    "Convert French to English"
    translation=''
    if frenchtext is None or frenchtext=='':
        return translation
    translation = language_translator.translate(
    text=frenchtext,
    model_id='fr-en').get_result()
    
    englishtext=translation['translations'][0]['translation']
    
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    return englishtext
