class TrieNode:
    
    def __init__(self):
        self.is_end = 0
        self.children = {}
        

class Solution:
    
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        
        cur = self.root
        for s in word:
            if s not in cur.children:
                cur.children[s] = TrieNode()
            cur = cur.children[s]
        
        cur.is_end += 1
    
    def search(self, s, index, root):
        
        count = 0
        if index == len(s):
            return count
        
        char = s[index]
        for key in root.children:
            # if matched:
            
            cur_index = index
            cur_char = ""
            
            while cur_char != key and cur_index < len(s):
                cur_char = s[cur_index]
                cur_index += 1
                
            if key == cur_char and root.children[key].is_end:
                count += root.children[key].is_end
                
            count += self.search(s, cur_index, root.children[key])
                
        return count
        
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # build the prefix tree
        for word in words:
            self.add(word)
        
        root = self.root
        return self.search(s, 0, root)
        
        
        
        
        
        
        
        
        
        