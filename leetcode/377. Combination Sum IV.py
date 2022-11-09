# Link: https://leetcode.com/problems/combination-sum-iv/
#Q: 377. Combination Sum IV

# Top-down:

# Time: O(N)
# Space: O(N)

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [-1] *(200_001)
        
        def calculate(s):
            if s > target: return 0
            if s == target: return 1
            if dp[s] != -1: return dp[s]
            res = 0
            for x in nums:
                res += calculate(s + x)
            dp[s] = res
            return dp[s]
    
        return calculate(0)

# Bottom-up:

# Time: O(N)
# Space: O(N)

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for t in nums:
                if t <= i:
                    dp[i] += dp[i - t]
                    
        return dp[target]
        
        
        
        
