# Link: https://leetcode.com/problems/find-the-middle-index-in-array/
#Q: 1991. Find the Middle Index in Array

# Time: O(N)
# Space: O(N)

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        for i in range(1, n + 1):
            if prefix[i - 1] == prefix[-1] - prefix[i]:
                return i - 1
            
        return -1
