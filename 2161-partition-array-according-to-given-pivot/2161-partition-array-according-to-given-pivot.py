# Time: O(N)
# Space: O(N)

# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
#         before_pivot = []
#         after_pivot = []
        
#         count = 0
        
#         for index, value in enumerate(nums):
#             if value < pivot:
#                 before_pivot.append(value)
#             elif value > pivot:
#                 after_pivot.append(value)
#             else:
#                 count += 1
#         return before_pivot + [pivot] * count + after_pivot
    
    
# optimized

# Time: O(N)
# Space: O(N)

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
     
        n = len(nums)
        output = [0] * n
        
        low = 0
        similar = 0
        high = 0
        
        for index, value in enumerate(nums):
            if value < pivot:
                low += 1
            elif value == pivot:
                similar += 1
        
        high = low + similar
        similar = low
        low = 0
        
        for index, value in enumerate(nums):
            if value < pivot:
                output[low] = value
                low += 1
            elif value > pivot:
                output[high] = value
                high += 1
            else:
                output[similar] = value
                similar += 1
        
        return output
        



