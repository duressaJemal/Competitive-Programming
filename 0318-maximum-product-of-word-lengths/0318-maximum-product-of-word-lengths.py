class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        
        bits = []
        ofset = ord("a")
        res = 0
        
        for word in words:
            bit_mask = 0
            for char in word:
                bit_mask |= (1 << (ord(char) - ofset))
            bits.append(bit_mask)
        
        
        n = len(bits)
        for i in range(n):
            for j in range(i + 1, n):
                
                valid = True
                ln = max(int.bit_length(bits[i]), int.bit_length(bits[j]))
                
                left = bits[i]
                right = bits[j]
                
                index = 0
                
                while  index <= ln:
                    
                    l = ((left & (1 << index)) != 0)
                    r = ((right & (1 << index)) != 0)
                    
                    if l == r and l == True:
                        valid = False
                        break
                    
                    index += 1
                
                if valid:
                    res = max(res, len(words[i]) * len(words[j]))
            
        return res
                    
                
                
                    
                    
                    
                    
                    
                
                
                
                
                
            