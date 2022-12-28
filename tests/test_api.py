#/usr/bin/env python3
import unittest
import time
from SplinterlandsSDK.Api import Api

class TestSplinterlandsAPI(unittest.TestCase):
    def setUp(self):
        self.api = Api()

    def test_get_cards(self):
        # Make the API call
        cards = self.api.get_cards()
        # Verify that the response is a list
        self.assertIsInstance(cards, list)
        # Verify that the list is not empty
        self.assertTrue(cards)
        # Verify that each element in the list is a dictionary
        for card in cards:
            self.assertIsInstance(card, dict)
        # Verify that each card has an 'id' field
        for card in cards:
            self.assertIn('id', card)

    def test_caching(self):
        # First, clear the cache
        self.api.cache = {}
        # Make the first API call
        start_time = time.time()
        cards1 = self.api.get_cards()
        end_time = time.time()
        elapsed_time1 = end_time - start_time
        # Make the second API call
        start_time = time.time()
        cards2 = self.api.get_cards()
        end_time = time.time()
        elapsed_time2 = end_time - start_time
        # Verify that the data returned by the second call is the same as the first
        self.assertEqual(cards1, cards2)
        # Verify that the second call was much faster than the first, indicating that it was served from the cache
        self.assertLess(elapsed_time2, elapsed_time1 / 10)

    def test_get_settings(self):
        # Get the settings from the API
        settings = self.api.get_settings()
        # Assert that the settings are returned as a dictionary
        self.assertIsInstance(settings, dict)
        # Assert that the expected keys are present in the dictionary
        expected_keys = ["asset_url", "gold_percent", "starter_pack_price", "booster_pack_price", "market_fee", "num_editions",
                         "modern_num_editions", "core_editions", "starter_editions", "soulbound_editions", "event_creation_whitelist",
                         "ghost_creation_whitelist", "bat_event_list", "event_entry_fee_required", "max_event_entrants", "tournaments_creation_fee_dec",
                         "account", "stats", "rarity_pcts", "xp_levels", "alpha_xp", "gold_xp", "beta_xp", "beta_gold_xp", "combine_rates",
                         "combine_rates_gold", "battles"]
        for key in expected_keys:
            self.assertIn(key, settings)

    def test_get_specific_cards(self):
        uid = "C3-79-UUT7TSLVN4"
        expected_output = [
            {
                "uid": "C3-79-UUT7TSLVN4",
                "card_detail_id": 79,
                "player": "kiokizz.spt",
                "xp": 0,
                "combined_card_id": "C3-79-SYV98UHO68",
                "gold": False,
                "edition": 3,
                "alpha_xp": None,
                "details": {
                "id": 79,
                "name": "Highland Archer",
                "color": "Gray",
                "type": "Monster",
                "sub_type": None,
                "rarity": 1,
                "drop_rate": 0,
                "stats": {
                "mana": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                "attack": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                "ranged": [1, 1, 1, 2, 2, 2, 2, 2, 3, 3],
                "magic": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                "armor": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                "health": [2, 2, 3, 3, 3, 4, 4, 5, 4, 5],
                "speed": [1, 2, 2, 2, 3, 3, 4, 4, 4, 4],
                "abilities": [[], [], [], [], [], [], [], [], [], []],
            },
                "is_starter": False,
                "editions": "3",
                "created_block_num": None,
                "last_update_tx": None,
                "total_printed": 400004,
                "is_promo": False,
                "tier": None,
                "distribution": [
            {
                "card_detail_id": 79,
                "gold": False,
                "edition": 3,
                "num_cards": "52989",
                "total_xp": "3530775",
                "num_burned": "36153",
                "total_burned_xp": "1005420",
            },
            {
                "card_detail_id": 79,
                "gold": True,
                "edition": 3,
                "num_cards": "2307",
                "total_xp": "1058200",
                "num_burned": "1441",
                "total_burned_xp": "631600",
            },
            ],
            },
                "last_used_block": None,
                "last_used_player": None,
                "last_used_date": None,
            }
        ]
        actual_output = self.api.get_specific_cards(uid)
        self.assertEqual(actual_output, expected_output)

    def test_get_for_sale_grouped(self):
        # Invoke the get_for_sale_grouped function
        result = self.api.get_for_sale_grouped()

        # Verify that the result is a dictionary
        assert isinstance(result, list)

    def test_get_transaction(self):
        # Set up test data
        trx_id = "09c8ac9db08d246696fa795cbf03ff07b83303e6"
        result = self.api.get_transaction(trx_id)
        assert isinstance(result, dict)

    def test_get_player_market_history(self):
        player = "edition-x"
        result = self.api.get_player_market_history(player)
        assert isinstance(result, list)

if __name__ == '__main__':
    unittest.main()
