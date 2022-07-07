# link: https://leetcode.com/problems/jump-game-ii/submissions/

# time: O(n)
# space: O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        interval = [0, 0]
        can_reach = 0
        jumps = 0
        
        while can_reach < (n - 1):
            jumps += 1
            for i in range(interval[0], interval[1] + 1):
                can_reach = max(can_reach, i + nums[i])
            interval = [interval[1] + 1, can_reach]
            
        return jumps

    
# TopDown

# time: O(n)
# space: O(n)

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dp(i):
            
            if i == n - 1:
                return 1
            if i in memo:
                return memo[i]
            result = float("inf")
            for j in range(i + 1, min(n - 1, i + nums[i]) + 1):
                result = min(result, dp(j))
            memo[i] = result + 1
            return memo[i]
        
        return dp(0) - 1

        
