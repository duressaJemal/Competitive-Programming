# Link: https://leetcode.com/problems/permutation-in-string/
#Q: 567. Permutation in String

# Two pointer

# Time: O(N)
# Space: O(1) -- constant space(26 characters)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        
        n, l = len(s2), 0
        
        for r in range(n):
            counter[s2[r]] -= 1 # add()
            while counter[s2[r]] < 0: # good()
                counter[s2[l]] += 1 # remove()
                l += 1
            
            if r - l + 1 == len(s1): # additional check
                return True
            
        return False
