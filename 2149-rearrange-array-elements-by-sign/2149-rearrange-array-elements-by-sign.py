class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        positive_index = 0
        negative_index = 0
        
        output = []
        
        while positive_index < n and negative_index < n:
            
            while positive_index < n and nums[positive_index] < 0:
                positive_index += 1
            
            while negative_index < n and nums[negative_index] > 0:
                negative_index += 1
            
            # check if the index are valid
            if positive_index < n and negative_index < n:
                output.append(nums[positive_index])
                output.append(nums[negative_index])
            
                positive_index += 1
                negative_index += 1
            
        return output
            
        