#!/usr/bin/env python3

class Card:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.color = data['color']
        self.card_type = data['type']
        self.sub_type = data['sub_type']
        self.rarity = data['rarity']
        self.drop_rate = data['drop_rate']
        self.mana_cost = data['stats']['mana'][0]
        self.health = data['stats']['health'][0]
        self.attack = data['stats']['attack'][0]
        self.speed = data['stats']['speed'][0]
        self.abilities = data['stats']['abilities'][0]
        self.is_starter = data['is_starter']
        self.editions = data['editions']
        self.created_block_num = data['created_block_num']
        self.last_update_tx = data['last_update_tx']
        self.total_printed = data['total_printed']
        self.is_promo = data['is_promo']
        self.tier = data['tier']
        self.distribution = data['distribution']

    @classmethod
    def get_card_info(cls, api, card_id):
        cards = api.get_cards()
        for card in cards:
            if card['id'] == card_id:
                return cls(card)
        raise ValueError(f"Card with ID {card_id} not found")

    @staticmethod
    def get_rarities() -> dict:
        rarities: dict = {
            1: "common",
            2: "rare",
            3: "epic",
            4: "legendary"
        }
        return rarities

    @staticmethod
    def get_colors() -> dict:
        colors: dict = {
            "Red": "fire",
            "Blue": "water",
            "Green": "earth",
            "White": "life",
            "Black": "death",
            "Gold": "dragon",
            "Gray": "neutral"
        }
        return colors

    @staticmethod
    def get_editions() -> dict:
        editions: dict = {
            "alpha": 0,
            "beta": 1,
            "promo": 2,
            "reward": 3,
            "untamed": 4,
            "dice": 5,
            "chaos": 7,
            "rift": 8
        }
        return editions


