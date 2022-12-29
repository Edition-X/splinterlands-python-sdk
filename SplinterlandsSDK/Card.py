from SplinterlandsSDK import Api
#!/usr/bin/env python3
class Card:

    def __init__(self, cardid, gold=False) -> None:
        self.api           = Api()
        self.cardid        = cardid
        self.gold          = gold
        self.name          = self.get_name()
        self.low_price_bcx = self.get_low_price_bcx()

    def get_name(self):
        self.all_cards = self.api.get_cards()
        return next(card["name"] for card in self.all_cards if card["id"] == self.cardid)

    def get_low_price_bcx(self):
        self.sale_data = self.api.get_for_sale_grouped()
        return next(card["low_price_bcx"] for card in self.sale_data if card["card_detail_id"] == self.cardid and card["gold"] == self.gold)


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


