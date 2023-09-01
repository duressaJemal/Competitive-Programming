class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]
        
        for i in range(1, n + 1):
            output.append(self.check(i))
        
        return output
    
    def check(self, num):
        count = 0
        bit = 1
        
        while bit <= num:

            if bit & num != 0:
                count += 1
            bit = bit << 1
        
        return count
    
    
    
        
            
            
        
        
            
        