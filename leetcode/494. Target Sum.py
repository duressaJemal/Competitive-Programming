# Link: https://leetcode.com/problems/target-sum/
#Q: 494. Target Sum

# Top-down

# Time: O(N * T)
# Space: O(N * T)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        dp = [[-1] * (2 * total + 1) for _ in range(len(nums))]
        
        def calculate(i, SUM):
            if i == len(nums):
                if SUM == target:
                    return 1
                return 0
            
            if dp[i][SUM + total] != -1: return dp[i][SUM + total]
            dp[i][SUM + total] = calculate(i + 1, SUM + nums[i]) + calculate(i + 1, SUM - nums[i])
            return dp[i][SUM + total]
        
        return calculate(0, 0)
    
    


# Bottom-up

# Time: O(N*T) where T = sum(nums)
# Space: O(N*T):

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        dp = [[0] * (2 * total + 1 ) for _ in range(len(nums))]
        dp[0][nums[0] + total] = 1
        dp[0][-nums[0] + total] += 1
        
        for i in range(1, len(nums)):
            for j in range(-total, total + 1):
                left = j - nums[i] + total
                right = j + nums[i] + total
                
                if left < 0:
                    dp[i][j + total] = dp[i  - 1][right]
                elif right >= (2 * total + 1):
                    dp[i][j + total] = dp[i - 1][left]
                else:
                    dp[i][j + total] = dp[i - 1][left] + dp[i - 1][right] 
        
        return dp[len(nums) - 1][target + total] if target <= total else 0
    
    
    
# recursion(TLE)

# Time: O(2^N)
# Space: O(N)

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
#         self.count = 0
#         def calculate(i, SUM):
#             if i == len(nums):
#                 if SUM == target:
#                     self.count += 1
#             else:
#                 calculate(i + 1, SUM - nums[i])
#                 calculate(i + 1, SUM + nums[i])
            
#         calculate(0, 0)
#         return self.count
