# Link: https://leetcode.com/problems/domino-and-tromino-tiling/
#Q: 790. Domino and Tromino Tiling

# Bottom-up

# Time: O(N*2)
# Space: O(N)

class Solution:
    def numTilings(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if j < 3:
                    dp[i] += dp[i - j]
                else:
                    dp[i] += 2 * dp[i - j]
            
        return dp[n] % (10**9 + 7)
    

# Top-down

# Time: O(N*2)
# Space: O(N)
class Solution:
    def numTilings(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        
        def helper(i):
            if i < 2: return 1
            if dp[i] != 0: return dp[i]
            
            for j in range(1, i + 1):
                if j < 3:
                    dp[i] += helper(i - j)
                else:
                    dp[i] += 2 * helper(i - j)
            
            return dp[i]
        
        return helper(n) % (10 ** 9 + 7)
            
