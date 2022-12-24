# Link: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
#Q: 1930. Unique Length-3 Palindromic Subsequences

# Time: O(N*26)
# Space: O(N)

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        last_index = defaultdict(int)
        for index, value in enumerate(s):
            last_index[value] = index
        
        output = set()
        visited = set()
        
        for i in range(len(s)):
            if s[i] not in visited:
                if len(visited) == 26:
                    break
                start = i
                end = last_index[s[i]]
                for j in range(i + 1, end):
                    output.add(s[start] + s[j] + s[end])
                visited.add(s[i])
                
        return len(output)
     
        
# Wrong Answer

#         n = len(s)
#         prefix = [[0 for _ in range(26)] for _ in range(n)]
#         prefix[0][ord("a") - ord(s[0])] = 1
        
#         for i in range(1, n):
#             current = prefix[i - 1].copy()
#             current[ord(s[i]) - ord("a")] += 1
#             prefix[i] = current.copy()
        
#         output = set()
        
#         for i in range(1, n - 1):
#             for j in range(26):

#                 before_current = prefix[i - 1][j]
#                 after_current = prefix[-1][j] - prefix[i][j]

#                 if before_current and after_current:
#                     output.add(chr(ord("a") + j) + s[i] + chr(ord("a") + j))

#         return len(output)
                
            
