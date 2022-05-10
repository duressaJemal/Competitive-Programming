class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        pre = [1] * (n + 1)
        post = [1] * (n + 1)
        output = [0]* n
        
        for i in range(1, len(nums) + 1): #pre
            pre[i] = pre[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 1, -1, -1): #post
            post[i] = post[i + 1] * nums[i]
        
        for i in range(len(output)): # output at each index
            output[i] = pre[i] * post[i + 1]
        
        return output
