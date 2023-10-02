class TrieNode:
    
    def __init__(self):
        
        self.is_end = False
        self.children = {}
        
class WordDictionary:

    def __init__(self):

        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        
        cur = self.root
        for s in word:
            if s not in cur.children:
                cur.children[s] = TrieNode()
            cur = cur.children[s]
        
        cur.is_end = True
                
            
    def search(self, word: str, root = None) -> bool:
        
        cur = root if root else self.root
        n = len(word)
        
        for i in range(n):
            s = word[i]
            if s == ".":

                # iterate over all possible
                for key in cur.children:
                    if self.search(word[i + 1:], cur.children[key]):
                        return True
                    
                return False
                    
            if s not in cur.children:
                return False
            cur = cur.children[s]
        
        return cur.is_end



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)