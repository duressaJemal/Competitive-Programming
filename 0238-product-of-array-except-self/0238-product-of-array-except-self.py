# Time: O(N)
# Space: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        current_product = 1
        
        # build sufix
        sufix = [1] * (n + 1)
        for index in range(n - 1, -1, -1):
            sufix[index] = sufix[index + 1] * nums[index]
        
        for index in range(n):
            sufix[index] = current_product * sufix[index + 1]
            current_product *= nums[index]
        
        sufix.pop()
        return sufix