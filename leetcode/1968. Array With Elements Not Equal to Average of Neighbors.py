class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        n = len(nums)
        output = [0] * n # for storing output list elements
        
        median = nums[n//2 -1] if n % 2 == 0 else nums[n//2] # finds the median value
        
        next_odd = 0
        next_even = 1
        
        for i in range(n):
            
            if nums[i] <= median and next_odd < n:
                output[next_odd] = nums[i]
                next_odd += 2
                continue
                
            if next_even < n: # if nums[i] is not <= median, it > median
                output[next_even] = nums[i]
                next_even += 2

        return output
