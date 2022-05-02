class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        unique = set() # for storing unique value in traversal
        s.replace(" ", "") # remove all white spaces
        
        start = 0
        end = 0
        longest = 0
        
        while end < len(s) and start < len(s):
            
            if s[end] in unique: # shrinking condition
                unique.remove(s[start])
                start += 1
                
            else: # expand
                
                unique.add(s[end]) # add unique value to set
                longest = max(longest, end - start + 1)
                end += 1
                
        return longest
