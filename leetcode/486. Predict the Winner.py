# link: https://leetcode.com/problems/predict-the-winner/solution/

# TopDown

# time: O(n ** 2)
# space: O(n ** 2)

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        memo = {}
        m = 0
        n = len(nums) - 1
        
        def dp(nums, i, j, memo):
            
            if i == j:
                return nums[i]
            
            if i > j:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = max(nums[i] + min(dp(nums, i + 1, j - 1, memo), dp(nums, i + 2, j, memo)), nums[j] + min(dp(nums, i + 1, j - 1, memo), dp(nums, i, j - 2, memo)))
            
            
            return memo[(i, j)]
        
        player1 = dp(nums, m, n, memo)
        
        
        return player1 >= sum(nums) - player1
    

        

            
    
        
