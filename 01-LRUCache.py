class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict()
        self.recent_keys = []
        self.capacity = capacity
        
    def cache(self, key):
        if key not in self.recent_keys:
            self.recent_keys.append(key)
        else:
            self.recent_keys.remove(key)
            self.recent_keys.append(key)

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            LRU_Cache.cache(self,key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        cache = self.cache
        capacity = self.capacity
        if key not in cache:
            cache[key] = value
        LRU_Cache.cache(self,key)
        if len(cache) == capacity + 1:
            cache.pop(self.recent_keys[0])
            self.recent_keys.pop(0)

    
# TESTS
our_cache = LRU_Cache(5)

print(our_cache.cache)
# returns {} because the cache is a dictionary

our_cache.set(1, 10)

print(our_cache.cache)
# returns {1: 10}
print(our_cache.recent_keys)
# returns [1]

our_cache.set(2, 2)

print(our_cache.cache)
# returns {1: 10, 2:2}
print(our_cache.recent_keys)
# returns [1, 2]

our_cache.set(1, 10)

# Test for setting a duplicate key, and test to make sure recent_keys is updated
print(our_cache.cache)
# returns {1: 10, 2:2}
print(our_cache.recent_keys)
# returns [2, 1]

our_cache.set(3, 3)

print(our_cache.cache)
# returns {1: 10, 2:2, 3:3}
print(our_cache.recent_keys)
# returns [2, 1, 3]

our_cache.set(4, 4)

print(our_cache.cache)
# returns {1: 10, 2: 2, 3: 3, 4: 4}
print(our_cache.recent_keys)
# returns [2, 1, 3, 4]

our_cache.set(5, 5)

print(our_cache.cache)
# returns {1: 10, 2: 2, 3: 3, 4: 4, 5: 5}
print(our_cache.recent_keys)
# returns [2, 1, 3, 4, 5]

our_cache.set(6, 6)

print(our_cache.cache)
# returns {1: 10, 3: 3, 4: 4, 5: 5, 6: 6}
print(our_cache.recent_keys)
# returns [1, 3, 4, 5, 6]

print(our_cache.get(1))
# returns 10

print(our_cache.recent_keys)
# returns [3, 4, 5, 6, 1]

print(our_cache.get(2))
# returns -1 because 2 is not currently present in the cache, it was dropped when we added (6,6)