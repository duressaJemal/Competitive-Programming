# Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/
#Q: 438. Find All Anagrams in a String

# Two pointer

# Time: O(N) -- N = len(p) + len(s)
# Space: O(N)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        counter = Counter(p)
        l, res = 0, []
        
        for r in range(len(s)):
            counter[s[r]] -= 1 # add()
            while counter[s[r]] < 0: # good()
                counter[s[l]] += 1 # remove()
                l += 1
                
            if r - l + 1 == len(p): # extra check
                res.append(l)
                
        return res
                
            
        
            
