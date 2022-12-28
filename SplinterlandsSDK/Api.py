#/usr/bin/env python3
from typing import List, Union
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

    def _make_request(self, endpoint: str, params: dict = {}) -> Union[dict, List]:
        # If the data is not in the cache, make the API request
        url: str = f"{self.base_url}/{endpoint}"
        response: requests.Response = requests.get(url, params=params, headers=self._get_headers())
        if response.status_code != 200:
            print(f"Request to {url} failed with status code {response.status_code}")
            return []
        data: dict = response.json()
        return data

    def get_cards(self) -> Union[dict, List]:
        endpoint: str = "cards/get_details"
        # Check if the data is already in the cache
        cache_key: str = f"{endpoint}"
        if  cache_key in self.cache:
            cached_data, cache_timestamp = self.cache[cache_key]
            age = time.time() - cache_timestamp
            if age < (30 * 24 * 60 * 60):  # 30 days
                return cached_data
        # Make the API request
        data = self._make_request(endpoint)
        # Save the data in the cache
        self.cache[cache_key] = (data, time.time())
        return data


    def get_settings(self) -> Union[dict, List]:
        endpoint: str = "settings"
        return self._make_request(endpoint)

    def get_specific_cards(self, uid: str) -> Union[dict, List]:
        endpoint: str = f"cards/find?ids={uid}"
        return self._make_request(endpoint)

    def get_for_sale_grouped(self) -> Union[dict, List]:
        endpoint: str = "market/for_sale_grouped"
        return self._make_request(endpoint)

    def get_transaction(self, trx_id: str) -> Union[dict, List]:
        endpoint: str = f"transactions/lookup?trx_id={trx_id}"
        return self._make_request(endpoint)

    def get_player_market_history(self, player: str) -> Union[dict, List]:
        endpoint: str = f"market/history?player={player}"
        return self._make_request(endpoint)
