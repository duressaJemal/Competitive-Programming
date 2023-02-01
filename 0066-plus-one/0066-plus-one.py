class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        
        for index in range(n - 1, -1, -1):
            if digits[index] < 9:
                digits[index] += 1
                return digits
            else:
                digits[index] = 0
        
        # happens if all the given digits are bunch of nines
        
        output = [0] * (n + 1)
        output[0] = 1
        
        return output