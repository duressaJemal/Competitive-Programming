class Solution:
    def smallerNumbersThanCurrent(self, nums):
        output=[]
        for i in range(len(nums)):
            counter = 0
            min = nums[i]
            for j in range(len(nums)):
                
                if min > nums[j]:
                    counter += 1
            
            output.append(counter)
        return output
