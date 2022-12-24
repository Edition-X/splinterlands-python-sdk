#/usr/bin/env python3
import unittest
import time
import sys
sys.path.insert(0, '..')
from SplinterlandsAPI import SplinterlandsAPI

class TestSplinterlandsAPI(unittest.TestCase):
    def setUp(self):
        self.api = SplinterlandsAPI()

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

if __name__ == '__main__':
    unittest.main()
