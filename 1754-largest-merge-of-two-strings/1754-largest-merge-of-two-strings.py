class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        word1 = list(word1)
        word2 = list(word2)
        
        merge = []
        
        while word1 or word2:
            
            if word1 >= word2:
                merge.append(word1.pop(0))
            else:
                merge.append(word2.pop(0))
        
        return "".join(merge)
            