#!/usr/bin/python3
"""LIFO cache impelementation"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """A caching class to handle caching using LIFO structure"""
    def __init__(self):
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """ Assign to the dictionary, LIFO algorithm, add element """
        if key and item:
            # Assigning to the dictionary
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Let's remove the item
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key
    
    def get(self, key):
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
