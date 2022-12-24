#/usr/bin/env python3
import requests
import time
import json

class Api:
    def __init__(self) -> None:
        self.base_url: str = "https://api.splinterlands.com"
        self.cache: dict = {}


    def _get_headers(self) -> dict:
        return {
        }

    def _make_request(self, endpoint: str, params: dict = {}) -> dict:
        # Check if the data is already in the cache
        cache_key: str = f"{endpoint}:{json.dumps(params)}"
        if cache_key in self.cache:
            cached_data, cache_timestamp = self.cache[cache_key]
            age = time.time() - cache_timestamp
            if age < 300:  # 5 minutes
                return cached_data

        # If the data is not in the cache, make the API request
        url: str = f"{self.base_url}/{endpoint}"
        response: requests.Response = requests.get(url, params=params, headers=self._get_headers())
        if response.status_code != 200:
            raise Exception(f"Request to {url} failed with status code {response.status_code}")
        data: dict = response.json()

        # Save the data in the cache
        self.cache[cache_key] = (data, time.time())
        return data

    def get_cards(self) -> dict:
        endpoint: str = "cards/get_details"
        return self._make_request(endpoint)

    def get_settings(self) -> dict:
        endpoint: str = "settings"
        return self._make_request(endpoint)

    def get_specific_cards(self, uid: str) -> dict:
        endpoint: str = f"cards/find?ids={uid}"
        return self._make_request(endpoint)
