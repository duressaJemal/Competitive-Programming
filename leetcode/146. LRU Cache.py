link: https://leetcode.com/problems/lru-cache/

time: O(n*2)
space: O(n)

class LRUCache:

    def __init__(self, capacity: int):
        self.recent = deque([])
        self.lru = {}
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        
        if key in self.lru:
            self.recent.remove(key)
            self.recent.append(key)
            return self.lru[key]
        
        return -1
            

    def put(self, key: int, value: int) -> None:
        
        # updated queue and add the key, value pairs to lru
        if key in self.lru:
            self.lru[key] = value
            self.recent.remove(key)
            self.recent.append(key)
            return
        
        # remove the least recent and add the current key, value pair
        if len(self.lru) >= self.capacity:
            evict = self.recent.popleft()
            self.lru.pop(evict)

        self.lru[key] = value
        self.recent.append(key)
        
