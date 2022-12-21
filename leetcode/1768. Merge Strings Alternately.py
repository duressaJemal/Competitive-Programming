# Link: https://leetcode.com/problems/merge-strings-alternately/
#Q: 1768. Merge Strings Alternately

# Time: O(N + M)
# Space: O(N + M)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
            
        output = []
        l, r = 0, 0  
        while l < len(word1) or r < len(word2):
            if l < len(word1):
                output.append(word1[l])
                l += 1
            if r < len(word2):
                output.append(word2[r])
                r += 1
        
        return "".join(output)
            
            
            
