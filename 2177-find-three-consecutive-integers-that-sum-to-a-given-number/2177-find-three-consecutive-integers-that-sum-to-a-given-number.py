class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        """
        x, x + 1, x + 2 = 3x + 3 
        
        then 3(x + 1) = num
        
        if num % 3 == 0:
            x = (num / 3) - 1
            return [x, x + 1, x + 2]
        else:
            return false
        
        """
        
        if num % 3 == 0:
            start = (num // 3) - 1
            return [start, start + 1, start + 2]
        else:
            return []
        
        