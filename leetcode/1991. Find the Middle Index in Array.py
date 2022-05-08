class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        prefix = [0] * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        for i in range(1, len(prefix)):
            if prefix[i-1] == prefix[-1] - prefix[i]:
                return i-1
            
        return - 1
