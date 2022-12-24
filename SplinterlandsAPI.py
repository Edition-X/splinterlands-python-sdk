#/usr/bin/env python3
import requests
import time
import json

class SplinterlandsAPI:
    def __init__(self):
        self.base_url = "https://api.splinterlands.com"
        self.cache = {}


    def _get_headers(self):
        return {
        }

    def _make_request(self, endpoint, params=None):
        if not params:
            params = {}
        # Check if the data is already in the cache
        cache_key = f"{endpoint}:{json.dumps(params)}"
        if cache_key in self.cache:
            cached_data, cache_timestamp = self.cache[cache_key]
            age = time.time() - cache_timestamp
            if age < 300:  # 5 minutes
                return cached_data

        # If the data is not in the cache, make the API request
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params, headers=self._get_headers())
        if response.status_code != 200:
            raise Exception(f"Request to {url} failed with status code {response.status_code}")
        data = response.json()

        # Save the data in the cache
        self.cache[cache_key] = (data, time.time())
        return data

    def get_cards(self):
        endpoint = "cards/get_details"
        return self._make_request(endpoint)

    def get_settings(self):
        endpoint = "settings"
        return self._make_request(endpoint)

    def get_specific_cards(self, uid):
        endpoint = f"cards/find?ids={uid}"
        return self._make_request(endpoint)
