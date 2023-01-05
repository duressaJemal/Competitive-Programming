class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0] * n
        for index, value in  enumerate(nums):
            ans[index] = nums[value]
        
        return ans