#!/usr/bin/python3
"""FIFOCache class that inherits from BaseCaching class
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """"""
    
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item
        """Checking if the items number reachs Max item number"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the first item FIFO
            print('DISCARD: ', self.cache_data[0].key, '\n')
    
    def get(self, key):
        if key is None:
            return None
        return self.cache_data.get(key)

