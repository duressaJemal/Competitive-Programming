class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        string = []
        for digit in digits:
            string.append(str(digit))
        
        digits = "".join(string)
        digits = int(digits)
        digits += 1
        
        digits = str(digits)
        
        output = []
        for digit in digits:
            output.append(int(digit))
        
        return output