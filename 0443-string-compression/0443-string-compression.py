# Time: O(N^2)
# Space: O(1)

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n = len(chars)
        
        left = 0
        right = 0
        
        while right < n:
            
            cur = chars[left]
            count = -1
            
            while right < n and chars[right] == cur:
                right += 1
                count += 1
            
            if count:
                str_count = str(count + 1)
                left += 1
                
                for char in str_count:
                    chars[left] = char
                    left += 1
                
                # remove unwanted
                while left != right:
                    chars[left] = "-1"
                    left += 1
            
        
            # adjust
            left = right
        
        index = 0
        
        while index < len(chars):
            
            if chars[index] == "-1":
                chars.pop(index)
            else:
                index += 1
            
        
        
        
        
        
            
            
            
            
            