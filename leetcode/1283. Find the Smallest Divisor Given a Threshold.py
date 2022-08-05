# Link: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

# Binary search

# Time: O(N * log(N))
# Space: O(1)

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        start, end = 1, max(nums)
        while start < end:
            mid = start + (end - start) // 2
            SUM = sum(ceil(num / mid) for num in nums)
            if threshold < SUM:
                start = mid + 1
            else:
                end = mid       
        return end
    
    
