#!/usr/bin/env python3
from beem import Hive
class Hive:
    def __init__(self, hive_active_key) -> None:
        self.hive = Hive(keys=hive_active_key)

    def custom_json(self, message, json, account):
        try:
            self.hive.custom_json(message, json_data=json, required_auths=[account])
        except Exception as e:
            raise Exception(f"error occoured while sending custom json message: {message} with error: {repr(e)}")

