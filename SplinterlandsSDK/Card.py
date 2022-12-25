#!/usr/bin/env python3
class Card:
    def __init__(self):
        pass

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


