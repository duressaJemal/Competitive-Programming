class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        counter = {}
        
        for index, num in enumerate(nums):
            
            if target - num in counter:
                return [index, counter[target - num]]
            else:
                counter[num] = index
        
        
            