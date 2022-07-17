# link: https://leetcode.com/problems/two-sum/

# time: O(n)
# space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        counter = {}
        
        for i in range(len(nums)):
            
            num = target - nums[i]
            if num in counter:
                return [counter[num], i]
            
            else:
                if nums[i] not in counter:
                    counter[nums[i]] = i
        
        
