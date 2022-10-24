# Link: https://leetcode.com/problems/perfect-squares/
#Q: 279. Perfect Squares
# Top-down

# Time: O(N*K) where k = len(perfec_square)
# Space: O(N)

class Solution:
    def numSquares(self, n: int) -> int:
        
        perfect_square = []
        for i in range(1, n):
            if i * i > n:
                break
            perfect_square.append(i * i)
        
        MAX = float("inf")
        dp = [MAX for _ in range(n + 1)]
        dp[0], dp[1] = 0, 1
        
        for num in perfect_square:
            for i in range(num, n + 1):
                dp[i] = min(dp[i], dp[i - num] + 1)
                
        return dp[n]
            
