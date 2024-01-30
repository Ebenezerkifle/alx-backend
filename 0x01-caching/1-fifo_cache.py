#!/usr/bin/python3
""" FIFO Cache class that inherits from BaseCaching class
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system """
    
    def __init__(self):
        super().__init__()
        self.data = {}
        self.next_in, self.next_out = 0, 0
    
    def put(self, key, item):
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self._push(key, item)
        """Checking if the items number reachs Max item number"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the first item FIFO
            print('DISCARD: ', self.cache_data[0].key, '\n')
    
    def get(self, key):
        """ Return the value linked """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value

    def _push(self, key, item):
        """ FIFO algorithm, add element """ 
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.next_out + 1]))
            self._pop()
        self.cache_data[key] = item
        self.next_in += 1
        self.data[self.next_in] = key

    def _pop(self):
        """FIFO algorithm to remove an element"""
        self.next_out += 1
        key = self.data[self.next_out]
        del self.data[self.next_out], self.cache_data[key]
