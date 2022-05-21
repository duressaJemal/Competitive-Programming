# link https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        memo = {}
        def helper(target, nums):
            
            if target in memo: return memo[target]
            if target == 0: return 1
            if target < 0: return 0
            
            total = 0
            for num in nums:
                remainder = target - num
                total += helper(remainder, nums)
            
            memo[target] = total
            return total
        
        return helper(target, nums)

    

                
