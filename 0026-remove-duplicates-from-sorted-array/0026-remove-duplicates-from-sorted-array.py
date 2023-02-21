class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 0
        
        for index in range(1, n):
            if nums[index] == nums[index - 1]:
                nums[index - 1] = 101 # out of boundary max
                count += 1
        
        nums.sort()
        return n - count
        
        
        