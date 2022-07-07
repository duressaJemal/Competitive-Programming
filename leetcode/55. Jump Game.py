# link: https://leetcode.com/problems/jump-game/submissions/

# time: O(n)
# space: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        can_reach = 0
        n = len(nums)
        
        i = 0
        while i <= can_reach:
            if i == n - 1:
                return True
            can_reach = max(can_reach, i + nums[i])
            i += 1
        
        return False


# TopDown(memoization)

# time: O(n)
# space: O(n)

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
        
#         n = len(nums)
#         memo = {}
#         memo[n - 1] = True
        
#         def dp(i):
            
#             if i in memo:
#                 return memo[i]
            
#             if i == n - 1:
#                 return memo
            
#             for j in range(i + 1, min(i + nums[i], n - 1) + 1):
#                 if dp(j):
#                     memo[i] = True
#                     return memo[j]
                
#             memo[i] = False
#             return memo[i]
        
#         return dp(0)

