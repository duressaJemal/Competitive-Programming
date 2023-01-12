class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        
        """
        create dictionary with key of nums[value] and value of index
        
        make every number represent index of nums
        after changing the given number to another number, make then new number           hold the index of array nums while removing the previous one
        
        
        
        
        """
        
        index_pointer = defaultdict(int)
        
        for index, value in enumerate(nums):
            index_pointer[value] = index
        
        for old, new in operations:
            nums[index_pointer[old]] = new
            index_pointer[new] = index_pointer[old]
        
        return nums
            
        
        
        
        
        