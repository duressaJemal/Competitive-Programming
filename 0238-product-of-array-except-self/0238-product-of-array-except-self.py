class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0] * n
        
        # build sufix
        sufix = [1] * (n + 1)
        for index in range(n - 1, -1, -1):
            sufix[index] = sufix[index + 1] * nums[index]
        
        # build prefix
        prefix = [1] * (n + 1)
        for index in range(1, n + 1):
            prefix[index] = nums[index - 1] * prefix[index - 1]
        
        for index in range(n):
            ans[index] = prefix[index] * sufix[index + 1]
        
        return ans