import requests
import os

authorization = os.environ['jwt']
org_name = os.environ['org_name']
base_url = 'https://proxy.query.ai/api/v1/'


class Client:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'Authorization': authorization})

    def get(self, path: str, payload: object=None, params: object=None):
        url = base_url + path
        try:
            response = self.session.get(url, json=payload, params=params)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        return response

    def post(self, path: str, payload: object=None, params: object=None):
        url = base_url + path
        try:
            response = self.session.post(url, json=payload, params=params)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        return response
