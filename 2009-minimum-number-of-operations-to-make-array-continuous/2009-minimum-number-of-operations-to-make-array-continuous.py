# Time: O(Nlog(N))
# Space: O(N)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        n_nums = [nums[0]]
        
        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                n_nums.append(nums[index])
            
        length_needed = len(nums)
        output = float("inf")
        
        for index, val in enumerate(n_nums):
            
            target = val + length_needed - 1
            target_index = bisect.bisect_right(n_nums, target)
            
            elements_between = target_index - index       
            
            output = min(output, length_needed - elements_between)
        
        return output
            