#!/usr/bin/env python3
from beem.blockchain import Blockchain
from beem import Hive
class Hive:
    def __init__(self, hive_active_key) -> None:
        self.hive = Hive(keys=hive_active_key)
        self.blockchain = Blockchain(blockchain_instance=self.hive, mode="head")

    def custom_json(self, account, message, json):
        try:
            self.hive.custom_json(message, json_data=json, required_auths=[account])
        except Exception as e:
            raise Exception(f"error occoured while sending custom json message: {message} with error: {repr(e)}")

