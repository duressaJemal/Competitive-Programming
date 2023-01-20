class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        output = []
        nums.sort()
        
        for index, value in enumerate(nums):
            if value == target:
                output.append(index)
        
        return output