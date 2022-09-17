# Link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/


# Top-Down (TLE)

# Time: O(K^2)
# Space: O(k^2)

# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
        
#         memo = {}
#         n = len(cardPoints)
        
#         def helper(l, opp):
#             if opp == k: return 0
            
#             if (l, opp) in memo: return memo[(l, opp)]
                
#             memo[(l, opp)] = max(cardPoints[l] + helper(l + 1, opp + 1), cardPoints[n - 1 - (opp - l)] + helper(l, opp + 1))
#             return memo[(l, opp)]
        
#         return helper(0, 0)

# Bottom-up

# Time: O(K^2)
# Space: O(K^2)

# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         n = len(cardPoints)
#         dp = [[0 for _ in range(k + 1)] for _ in range(k + 1)]
        
        
#         for opp in range(k - 1, -1, -1):
#             for l in range(opp, -1, -1):
#                 dp[opp][l] = max(cardPoints[l] + dp[opp + 1][l + 1], cardPoints[n - 1 - (opp - l)] + dp[opp + 1][l])
        
#         return dp[0][0]

# Pointer

# Time: O(n)
# Space: O(1)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        
        if k == n:
            return sum(cardPoints)
        
        left, right = 0, n - k - 1
        total = sum(cardPoints[:n - k])
        minimum = total
        
        while right < n:
        
            total -= cardPoints[left]
            left += 1
            
            if right == n - 1:
                break
            
            right += 1
            total += cardPoints[right]
            minimum = min(minimum, total)
        
        total = sum(cardPoints)
        
        return total - minimum
            
