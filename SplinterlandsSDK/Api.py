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
        url: str = f"{self.base_url}/{endpoint}"
        response: requests.Response = requests.get(url, params=params, headers=self._get_headers())
        if response.status_code != 200:
            raise Exception(f"Request to {url} failed with status code {response.status_code}")
        data: dict = response.json()
        return data

    def get_cards(self) -> Union[dict, List]:
        endpoint: str = "cards/get_details"
        return self._make_request(endpoint)

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
