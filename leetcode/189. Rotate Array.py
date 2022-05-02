class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        output = [0] * n
        
        for index, value in  enumerate(nums):
            output[(index + k) % n] = value
            
        for i in range(len(nums)):
            nums[i] = output[i]
            
        
            
