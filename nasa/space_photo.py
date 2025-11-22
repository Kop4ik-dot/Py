import requests

import deepl
API_KEY_DEEPL = "0bffabab-8341-453a-a518-3808f64987b8:fx"
deepl_client = deepl.DeepLClient(API_KEY_DEEPL)

class SpacePhoto:
    API_URL = "https://api.nasa.gov/planetary/apod"

    def __init__(self, api_key):
        self.api_key = api_key
        self.tittle = None
        self.description = None
        self.image_url = None

    def load(self):
        params = {
            "api_key": self.api_key
        }

        response = requests.get(self.API_URL, params=params)
        data = response.json()

        self.title = data.get("title", "Без назви")
        self.description = data.get("explanation", "Немає опису")
        self.image_url = data.get("url", "")


        self.description = deepl_client.translate_text(self.description, target_lang="UK")


    def show_info(self):
        print("Фото для NASA")
        print("Назва:", self.title)
        print("\n Опис:")
        print(self.description)
        print("\n Переглянути фото:")
        print(self.image_url)