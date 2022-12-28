from SplinterlandsSDK import Api
#!/usr/bin/env python3
class Card:

    def __init__(self, cardid, gold=False) -> None:
        self.api = Api()
        self.cardid = cardid
        self.gold = gold
        self.name = self.get_name()

    def get_name(self):
        self.all_cards = self.api.get_cards()
        for card in self.all_cards:
            if card["id"] == self.cardid:
                return card["name"]

    @classmethod
    def get_rarities(cls) -> dict:
        rarities: dict = {
            1: "common",
            2: "rare",
            3: "epic",
            4: "legendary"
        }
        return rarities

    @classmethod
    def get_colors(cls) -> dict:
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

    @classmethod
    def get_editions(cls) -> dict:
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


