# Time: O(1)
# Space: O(1)

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        if num % 3 == 0:
            start = (num // 3) - 1
            return [start, start + 1, start + 2]
        else:
            return []
        
        