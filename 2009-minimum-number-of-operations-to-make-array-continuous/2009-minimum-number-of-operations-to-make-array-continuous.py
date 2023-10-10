# Time: O(Nlog(N))
# Space: O(N)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n_nums = sorted(set(nums))
        
        length_needed = len(nums)
        output = float("inf")
        
        for index, val in enumerate(n_nums):
            
            target = val + length_needed - 1
            target_index = bisect.bisect_right(n_nums, target)
            
            elements_between = target_index - index       
            
            output = min(output, length_needed - elements_between)
        
        return output
            