# Link: https://leetcode.com/problems/palindromic-substrings/
#Q: 647. Palindromic Substrings

# Time: O(N*2)
# Space: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def countPalindrome(i, j):
            while i <= j:
                if s[i] != s[j]: return 0
                i += 1
                j -= 1
            return 1
    
        output = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                output += countPalindrome(i, j)
        
        return output
    

# Bottom-up

# Time: O(N*2)
# Space: O(N*2)

class Solution: 
    def countSubstrings(self, s: str) -> int:
        
        dp = [[0] * (len(s)) for _ in range(len(s))]
        count = 0
        
        for l in range(len(s)):
            for i in range(0, len(s) - l):
                j = i + l
                if i == j:
                    dp[i][j] = 1
                elif j == i + 1 and s[i] == s[j]:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                
                if dp[i][j]:
                    count += 1
        return count
    
# Top-down

# Time: O(N*2)
# Space: O(N*2)

class Solution: 
    def countSubstrings(self, s: str) -> int:
        
        memo = {}
        def helper(l, r):
            if l >= r: return 1
            if (l, r) in memo: return memo[(l, r)]
            memo[(l, r)] = helper(l + 1, r - 1) if s[l] == s[r] else 0
            return memo[(l, r)]
        
        count = 0
        for r in range(len(s)):
            for l in range(r + 1):
                count += helper(l, r)
        return count
