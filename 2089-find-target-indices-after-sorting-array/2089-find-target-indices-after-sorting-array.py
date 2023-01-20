# Time: O(N)
# Space: O(N)

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:     
        
        output = []
        
        less_than_target = 0
        equal_to_target = 0
        
        for num in nums:
            if num < target:
                less_than_target += 1
            elif num == target:
                equal_to_target += 1
        
        if equal_to_target:
            output += list(range(less_than_target, less_than_target + equal_to_target))
        
        return output


# Time: O(Nlog(N))
# Space: O(N)

# class Solution:
#     def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
#         output = []
#         nums.sort()
        
#         for index, value in enumerate(nums):
#             if value == target:
#                 output.append(index)
        
#         return output