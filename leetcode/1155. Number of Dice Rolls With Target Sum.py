# Link: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
#Q: 1155. Number of Dice Rolls With Target Sum

# Top-down

# Time: O(N*M) where M = len(target)
# Space: O(N*M) where M = len(target)

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        
        def helper(i, j):
            if j == 0 and i == 0: return 1
            if i == 0: return 0
            
            if dp[i][j] != -1: return dp[i][j]
            
            result = 0
            for m in range(1, k + 1):
                if m <= j:
                    result += helper(i - 1, j - m)
            
            dp[i][j] = result 
            return dp[i][j]
        
        return helper(n, target) % (10**9 + 7)

# Bottom-up

# Time: O(N*M) where M = len(target)
# Space: O(N*M) where M = len(target)

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:    
    
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                for m in range(1, k + 1):
                    if m <= j:
                        dp[i][j] += dp[i - 1][j - m]
                    
        return dp[n][target] % ((10 ** 9) + 7)
    
    
