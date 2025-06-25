import requests
from config.configtest import BASE_URL, COMMON_HEADERS

class PersonAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = COMMON_HEADERS

    def post_person(self, person_id):
        url = f"{self.base_url}/import"
        payload = [{"personId": person_id}]
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            return response
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}