#/usr/bin/env python3
import unittest
import time
import sys
sys.path.insert(0, '..')
from Card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
                self.data = {
                    'id': 79,
                    'name': 'Highland Archer',
                    'color': 'Gray',
                    'type': 'Monster',
                    'sub_type': None,
                    'rarity': 1,
                    'drop_rate': 0,
                    'stats': {
                        'mana': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                        'attack': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        'ranged': [1, 1, 1, 2, 2, 2, 2, 2, 3, 3],
                        'magic': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        'armor': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        'health': [2, 2, 3, 3, 3, 4, 4, 5, 4, 5],
                        'speed': [1, 2, 2, 2, 3, 3, 4, 4, 4, 4],
                        'abilities': [[], [], [], [], [], [], [], [], [], []]
                    },
                    'is_starter': False,
                    'editions': '3',
                    'created_block_num': None,
                    'last_update_tx': None,
                    'total_printed': 400004,
                    'is_promo': False,
                    'tier': None,
                    'distribution': [
                        {
                            'card_detail_id': 79,
                            'gold': False,
                            'edition': 3,
                            'num_cards': '52989',
                            'total_xp': '3530775',
                            'num_burned': '36153',
                            'total_burned_xp': '1005420'
                        },
                        {
                            'card_detail_id': 79,
                            'gold': True,
                            'edition': 3,
                            'num_cards': '2307',
                            'total_xp': '1058200',
                            'num_burned': '1441',
                            'total_burned_xp': '631600'
                        }
                    ]
                }
                self.card = Card(self.data)

    def test_card_init(self):
        # Check that the instance variables are set correctly
        self.assertEqual(self.card.id, self.data['id'])
        self.assertEqual(self.card.name, self.data['name'])
        self.assertEqual(self.card.color, self.data['color'])
        self.assertEqual(self.card.card_type, self.data['type'])
        self.assertEqual(self.card.sub_type, self.data['sub_type'])
        self.assertEqual(self.card.rarity, self.data['rarity'])
        self.assertEqual(self.card.drop_rate, self.data['drop_rate'])
        self.assertEqual(self.card.mana_cost, self.data['stats']['mana'][0])
        self.assertEqual(self.card.health, self.data['stats']['health'][0])
        self.assertEqual(self.card.attack, self.data['stats']['attack'][0])
        self.assertEqual(self.card.speed, self.data['stats']['speed'][0])
        self.assertEqual(self.card.abilities, self.data['stats']['abilities'][0])
        self.assertEqual(self.card.is_starter, self.data['is_starter'])
        self.assertEqual(self.card.editions, self.data['editions'])
        self.assertEqual(self.card.created_block_num, self.data['created_block_num'])
        self.assertEqual(self.card.last_update_tx, self.data['last_update_tx'])
        self.assertEqual(self.card.total_printed, self.data['total_printed'])
        self.assertEqual(self.card.is_promo, self.data['is_promo'])
        self.assertEqual(self.card.tier, self.data['tier'])
        self.assertEqual(self.card.distribution, self.data['distribution'])

if __name__ == '__main__':
    unittest.main()
