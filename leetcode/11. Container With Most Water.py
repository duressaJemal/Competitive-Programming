# link: https://leetcode.com/problems/container-with-most-water/

# time: O(n)
# space: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start, end, longest = 0, len(height) - 1, 0
        n = len(height)
        
        while start < end:
            area = (end - start) * min(height[start], height[end])
            longest = max(longest, area)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
                
        return longest
                
            
