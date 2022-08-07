# Link: https://leetcode.com/problems/h-index-ii/

# Binary search

# Time: O(log(N))
# Space: O(1)

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)
    
        left = 0 # assume first good value
        right = n # assume first bad value
        
        while right > left + 1:
            
            mid = (left + right) // 2
            if citations[mid] <= (n - mid):
                left = mid
            else:
                right = mid
                
        return max(citations[left], (n - left - 1)) if citations[left] <= (n - left) else (n - left)
    
        
