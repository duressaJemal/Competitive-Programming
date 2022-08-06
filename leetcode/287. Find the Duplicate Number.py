# Link: https://leetcode.com/problems/find-the-duplicate-number/

# Binary search

# Time: O(N * log(N))
# Space: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        start , end = 1, n - 1
        
        while start < end:
            mid = start + (end - start) // 2
            count = 0
            for i in range(0, n):
                count += 1 if nums[i] <= mid else 0
            if count > mid:
                end = mid
            else:
                start = mid + 1
        return start

                
                
