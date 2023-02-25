class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        
        unique = set()
        max_length = 0
        
        left = 0
        
        for right in range(n):
            
            # validate
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            
            # add
            unique.add(s[right])
            
            # record
            max_length = max(max_length, right - left + 1)
        
        
        return max_length
            
            
            