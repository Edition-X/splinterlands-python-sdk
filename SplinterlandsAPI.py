#/usr/bin/env python3
import requests

class SplinterlandsAPI:
    def __init__(self):
        self.base_url = "https://api.splinterlands.com"


    def _get_headers(self):
        return {
        }

    def _make_request(self, endpoint, params=None):
        if not params:
            params = {}
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params, headers=self._get_headers())
        if response.status_code != 200:
            raise Exception(f"Request to {url} failed with status code {response.status_code}")
        return response.json()

    def get_cards(self):
        endpoint = "cards/get_details"
        return self._make_request(endpoint)

    def get_settings(self):
        endpoint = "settings"
        return self._make_request(endpoint)
