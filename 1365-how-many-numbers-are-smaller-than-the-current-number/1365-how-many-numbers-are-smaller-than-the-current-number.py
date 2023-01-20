# Time: O(Nlog(N))
# Space: O(N)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        output = []
        sorted_num = sorted(nums)
        value_index = {}
        
        for index, value in enumerate(sorted_num):
            if value not in value_index:
                value_index[value] = index
        
        for num in nums:
            output.append(value_index[num])
        
        return output
                    