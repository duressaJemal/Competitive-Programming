class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        unique = set() # for storing unique value in traversal
        start, end, longest = 0, 0, 0
        n = len(s)
        
        if not n:
            return 0
        
        unique.add(s[start])
        for start in range(n):
            while end + 1 < n and s[end + 1] not in  unique:
                end += 1
                unique.add(s[end])
            
            longest = max(longest, end - start + 1)
            unique.remove(s[start])
            
        return longest
        
        
        
        
        
        
