# Link: https://leetcode.com/problems/verifying-an-alien-dictionary/
#Q: 953. Verifying an Alien Dictionary

# Time: O(M*N) where M = len(word), N = len(word[index])
# Space: O(26) = O(1)

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        position = {}
        for i in range(len(order)):
            position[order[i]] = i
        
        for i in range(1, len(words)):
            l, r = 0, 0
            len_l, len_r = len(words[i -1]), len(words[i])
            
            while l < len_l and r < len_r:
                if position[words[i - 1][l]] > position[words[i][r]]: 
                    return False
                if position[words[i - 1][l]] < position[words[i][r]]:
                    break
                l += 1
                r += 1
            
            if l < len_l and not r < len_r: return False
            
        return True
