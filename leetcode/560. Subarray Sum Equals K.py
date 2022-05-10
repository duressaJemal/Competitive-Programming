class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        summation = 0
        prefix = {0:1}
        output = 0
        
        for i in range(len(nums)):
            
            summation += nums[i]
            
            if summation - k in prefix:
                output += prefix[summation - k]
                
            if summation in prefix:
                prefix[summation] += 1
            else:
                prefix[summation] = 1
            
        return output
