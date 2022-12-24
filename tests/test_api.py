#/usr/bin/env python3
import unittest
import time
import sys
sys.path.insert(0, '..')
from SplinterlandsAPI import SplinterlandsAPI

class TestSplinterlandsAPI(unittest.TestCase):
    def setUp(self):
        self.api = SplinterlandsAPI()

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

if __name__ == '__main__':
    unittest.main()
