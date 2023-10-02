class TrieNode:
    
    def __init__(self):
        
        self.children = {}
        self.is_end = False
        self.value = 0

class MapSum:

    def __init__(self):
        
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        
        cur = self.root
        for s in key:
            if s not in cur.children:
                cur.children[s] = TrieNode()
            cur = cur.children[s]
        # we have reached the end
        cur.is_end = True
        cur.value = val
        

    def sum(self, prefix: str) -> int:
        cur = self.root
        for s in prefix:
            if s not in cur.children:
                return 0
            else:
                cur = cur.children[s]
        
        return self.sum_values(cur)
        
    
    def sum_values(self, root):
        
        total = root.value
        for key in root.children:
            total += self.sum_values(root.children[key])
        
        return total
        
        
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)