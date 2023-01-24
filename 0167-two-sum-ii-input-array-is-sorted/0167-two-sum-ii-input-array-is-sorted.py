# Time: O(N)
# Space: O(1)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        
        left = 0
        right = n - 1
        
        output = []
        
        while left < right:
            current = numbers[left] + numbers[right]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            else:
                output = [left + 1, right + 1]
                return output
        
