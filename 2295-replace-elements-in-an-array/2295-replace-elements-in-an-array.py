# Time: O(M + N)
# Space: O(N)

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        index_pointer = defaultdict(int)
        
        for index, value in enumerate(nums):
            index_pointer[value] = index
        
        for old, new in operations:
            nums[index_pointer[old]] = new
            index_pointer[new] = index_pointer[old]
        
        return nums
            
        
        
        
        
        