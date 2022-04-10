class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        i = 0
        j = i + 1
        n = len(nums)
        counter = 0
        
        while(i < n):
            
            while (j < n):
                
                if nums[i] == nums[j]:
                    counter += 1
                
                j += 1
            
            i += 1
            j = i + 1
        return counter
