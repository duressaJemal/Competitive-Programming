# Time: O(N)
# Space: O(N)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def dp(index, total):
            
            # base case
            if index == n:
                return 1 if total == target else 0

            return dp(index + 1, total + nums[index]) + dp(index + 1, total - nums[index])
            
        n = len(nums)
        return dp(0, 0)
            
            