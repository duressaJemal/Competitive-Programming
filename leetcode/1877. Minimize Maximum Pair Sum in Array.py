
class Solution:
    def minPairSum(self, nums):

        nums.sort()
        
        largest = 0
        for i in range(len(nums)//2):
            largest = max(largest, sum( (nums[-i-1], nums[i])))
            
        return largest
