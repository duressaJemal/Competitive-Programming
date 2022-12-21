# Link: https://leetcode.com/problems/find-the-difference/
#Q: 389. Find the Difference

# Time: O(N)
# Space: O(N)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        s, t = Counter(s), Counter(t)
        for key in t:
            if s[key] != t[key]:
                return key
        
