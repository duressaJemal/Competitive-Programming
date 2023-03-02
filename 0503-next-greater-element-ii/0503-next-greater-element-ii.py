# Time: O(N)
# Space: O(N)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        result = [-1] * (n)
        greater = []
        
        for index in range(2 * n):
            
            curr = index % n
            
            while greater and nums[curr] > nums[greater[-1]]:
                result[greater.pop()] = nums[curr]
            # add
            greater.append(curr)
        
        return result
            
            
            
            
        
        
    