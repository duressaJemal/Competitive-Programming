class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_num = sorted(nums)
        output = []
        
        for num in nums:
            for index, value in enumerate(sorted_num):
                if value == num:
                    break
            output.append(index)
        
        return output
                    