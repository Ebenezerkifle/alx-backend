#!/usr/bin/python3
""" A subclass of Base Caching module
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system
        This caching system doesn’t have limit """

    def put(self, key, item):
        """ Assign to the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        if key is None and self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
