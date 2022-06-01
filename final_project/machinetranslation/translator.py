"""
Translator powered by IBM Watson Language Translator
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


def create_translator_instance():
    """
    Create instance of ibm_watson transaltor with parameters fetched from .env
    """
    load_dotenv()

    apikey = os.environ['apikey']
    url = os.environ['url']
    version = os.environ['version']
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version=version,
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    return language_translator


class Translator():
    """ Wrapper for ibm_watson transaltor """

    def __init__(self):
        self.translator = create_translator_instance()

    def translate(self, text, model):
        """
        Translate text by seelcted model
        """
        if not text or not model:
            return None
        response = self.translator.translate(text=text, model_id=model)
        return response.result['translations'][0]['translation']

    def english_to_french(self, english_text):
        """
        Translate english text to french one
        """
        return self.translate(text=english_text, model="en-fr")

    def french_to_english(self, french_text):
        """
        Translate french text to english one
        """
        return self.translate(text=french_text, model="fr-en")
