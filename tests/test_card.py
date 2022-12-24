#/usr/bin/env python3
import unittest
import time
import sys
sys.path.insert(0, '..')
from Card import Card

class TestCard(unittest.TestCase):
    def test_card_init(self):
        data = {
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
        # Create an instance of the Card class
        card = Card(data)

        # Check that the instance variables are set correctly
        self.assertEqual(card.id, data['id'])
        self.assertEqual(card.name, data['name'])
        self.assertEqual(card.color, data['color'])
        self.assertEqual(card.card_type, data['type'])
        self.assertEqual(card.sub_type, data['sub_type'])
        self.assertEqual(card.rarity, data['rarity'])
        self.assertEqual(card.drop_rate, data['drop_rate'])
        self.assertEqual(card.mana_cost, data['stats']['mana'][0])
        self.assertEqual(card.health, data['stats']['health'][0])
        self.assertEqual(card.attack, data['stats']['attack'][0])
        self.assertEqual(card.speed, data['stats']['speed'][0])
        self.assertEqual(card.abilities, data['stats']['abilities'][0])
        self.assertEqual(card.is_starter, data['is_starter'])
        self.assertEqual(card.editions, data['editions'])
        self.assertEqual(card.created_block_num, data['created_block_num'])
        self.assertEqual(card.last_update_tx, data['last_update_tx'])
        self.assertEqual(card.total_printed, data['total_printed'])
        self.assertEqual(card.is_promo, data['is_promo'])
        self.assertEqual(card.tier, data['tier'])
        self.assertEqual(card.distribution, data['distribution'])

if __name__ == '__main__':
    unittest.main()
