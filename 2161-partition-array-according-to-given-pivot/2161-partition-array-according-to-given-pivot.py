# Time: O(N)
# Space: O(N)

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        before_pivot = []
        after_pivot = []
        
        count = 0
        
        for index, value in enumerate(nums):
            if value < pivot:
                before_pivot.append(value)
            elif value > pivot:
                after_pivot.append(value)
            else:
                count += 1
        return before_pivot + [pivot] * count + after_pivot