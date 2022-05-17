# link https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # build hash map : character and how often it appears
        counter = collections.Counter(s)
        
        #find the index
        for i in range(len(s)):
            if s[i] in counter and counter[s[i]] == 1:
                return i
        
        return -1
        
