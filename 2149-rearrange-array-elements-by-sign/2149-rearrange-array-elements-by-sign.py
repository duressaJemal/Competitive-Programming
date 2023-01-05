# Time: O(N)
# Space: O(N)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        positive_index = 0
        negative_index = 1
        
        output = [0] * n
        
        for value in nums:
            
            if value > 0:
                output[positive_index] = value
                positive_index += 2 # since we have to alternate the parity
            else:
                output[negative_index] = value
                negative_index += 2
            
        return output
            
        