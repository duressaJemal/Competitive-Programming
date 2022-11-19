# Link: https://leetcode.com/problems/longest-palindromic-substring/
#Q: 5. Longest Palindromic Substring

# Two-pointer

# Time: O(N*2)
# Space: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        mx_length = 0
        start_index = 0
        
        def checkPalindrome(i, j):
            nonlocal mx_length, start_index
            
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > mx_length:
                    mx_length = j - i + 1
                    start_index = i
                i -= 1
                j += 1
            return
                
        for i in range(len(s)):
            checkPalindrome(i, i)
            checkPalindrome(i, i + 1)
        
        return s[start_index : start_index + mx_length]


# Bottom-up

# Time: O(N*2)
# Space: O(N*2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        max_length = 0
        start_index = 0
        
        for l in range(n):
            for i in range(n - l):
                j = i + l
                # update dp
                dp[i][j] = (s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])) 
                
                # calculate max length
                if dp[i][j] and j - i + 1 > max_length:
                    max_length = j - i + 1
                    start_index = i
        return s[start_index : start_index + max_length]
    
    
#    ALTERNATIVE

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        long = (0, 0)
        
        for l in range(n):
            for i in range(n - l):
                j = i + l
                if i == j:
                    dp[i][j] = 1
                elif j == i + 1 and s[i] == s[j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                
                if dp[i][j]:
                    if j - i > long[1] - long[0]:
                        long = (i, j)
        return s[long[0] : long[1] + 1]
                    
                


# Top-down (TLE)

# Time: O(N*2)
# Space: O(N*2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        memo = {}
        def helper(i, j):
            if i >= j: return 1
            if (i, j) in memo: return memo[(i, j)]
            memo[(i, j)] = 1 if (s[i] == s[j] and helper(i + 1, j - 1)) else 0
            return memo[(i, j)]

        max_length = 0
        start_index = 0
        
        for r in range(len(s)):
            for l in range(r + 1):
                if helper(l, r):
                    if r - l + 1 > max_length:
                        max_length = r - l + 1
                        start_index = l
                
        return s[start_index : start_index + max_length]



                
        
        
                
                
