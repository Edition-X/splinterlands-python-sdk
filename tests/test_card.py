#/usr/bin/env python3
import unittest
import sys
sys.path.insert(0, '..')
from SplinterlandsSDK.Card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(1)

    def test_get_card_name(self):
        self.assertEqual(self.card.get_name(), "Goblin Shaman")
        self.card = Card(1, True)
        self.assertEqual(self.card.get_name(), "Goblin Shaman")

    def test_get_min_price_bcx(self):
        self.assertTrue(isinstance(self.card.low_price_bcx, float))

if __name__ == '__main__':
    unittest.main()
