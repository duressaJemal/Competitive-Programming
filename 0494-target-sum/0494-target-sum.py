class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dp(index, total):
            
            # base case
            if index == n:
                return 1 if total == target else 0
            
            if (index, total) in memo:
                return memo[(index, total)]
            
            memo[(index,total)] = dp(index + 1, total + nums[index]) + dp(index + 1, total - nums[index])
            
            return memo[(index, total)]
        
        n = len(nums)
        memo = defaultdict(int)
        return dp(0, 0)
            
            