# Link: https://leetcode.com/problems/partition-equal-subset-sum/
#Q: 416. Partition Equal Subset Sum

# Top-down

# Time: O(N*T) where T = total//2
# Space: O(N*T)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 != 0: return False
        total //= 2
        
        dp = [[-1] * (total + 1) for _ in range(len(nums))]
        
        def helper(i, j):
            
            if j == 0: return 1
            if i == 0: return 0
            
            if dp[i][j] != -1: return dp[i][j]
            
            include = helper(i - 1, j - nums[i])
            exclude = helper(i - 1, j)
            
            dp[i][j] = include or exclude
            return dp[i][j]
        
        return helper(len(nums) - 1, total) == 1
    
# Bottom-up

# Time: O(N*T)
# Space: O(N*T)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
       
        total = sum(nums)
        if total % 2 != 0: return False
        total //= 2
        
        dp = [[0] * (total + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            for j in range(total + 1):
                if j == 0:
                    dp[i][j] = 1 
                elif nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[i][j]
                
                
