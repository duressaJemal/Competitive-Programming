#link https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        odd_prefix = 0
        output = 0
        summation = {0:1}
        
        for i in range(len(nums)):
            
            if nums[i] % 2 != 0:
                odd_prefix += 1
       
            if odd_prefix - k in summation:
                output += summation[odd_prefix - k]
            
            if odd_prefix in summation:
                summation[odd_prefix] += 1
            else:
                summation[odd_prefix] = 1
            
        return output
