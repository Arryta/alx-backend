#!/usr/bin/env python3
"""
LRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache Class
    This is a caching class that uses LRU Algorithm
    """

    def __init__(self) -> None:
        """Initializes the LRUCache with a list of empty keys and dictionary
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Saves the item to the cache with the given key
        """
        if key and item:
            if key not in self.cache_data:
                self.keys.append(key)

            if len(self.keys) > self.MAX_ITEMS:
                rm_key = self.keys.pop(0)
                self.cache_data.pop(rm_key)
                print(f'DISCARD: {rm_key}')

            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to key or None if key
        is None or doesn't exist in self.cache_data
        """
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key)
