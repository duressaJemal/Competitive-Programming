# Link: https://leetcode.com/problems/2-keys-keyboard/submissions/
#Q: 650. 2 Keys Keyboard

# Top-down

# Time: O(N*2)
# Space: O(N)

class Solution:
    def minSteps(self, n: int) -> int:
        
        dp =  [i for i in range(n + 1)]
        dp[1] = 0
        
        for i in range(n + 1):
            for j in range(i // 2, 0, -1):
                if i % j == 0:
                    dp[i] = dp[j] + (i // j) 
                    # no need to checking other possibilities.
                    break
        return dp[n]

