class Trie:

    def __init__(self):
        
        self.root = TrieNode()
        self.ofset = ord("a")
        
    def insert(self, word: str) -> None:
        
        cur = self.root
        for s in word:
            key = ord(s) - self.ofset
            
            if not cur.children[key]:
                cur.children[key] = TrieNode(s)
            cur = cur.children[key]
                
        cur.is_end = True
            
        
    def search(self, word: str) -> bool:
        
        cur = self.root
        for s in word:
            key = ord(s) - self.ofset
            
            if cur.children[key]:
                cur = cur.children[key]
            else:
                return False
        
        return cur.is_end
        

    def startsWith(self, prefix: str) -> bool:
        
        cur = self.root
        for s in prefix:
            key = ord(s) - self.ofset
            
            if cur.children[key]:
                cur = cur.children[key]
            else:
                return False
        
        return True
        

class TrieNode:
    
    def __init__(self, val = None):
        
        self.val = val
        self.is_end = False
        self.children = [None for _ in range(26)]



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)