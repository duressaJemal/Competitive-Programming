class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        n = len(s)
        k = len(p)
        
        result = []
        
        counter_s = [0] * 26
        counter_p = [0] * 26
        
        # count
        for char in p:
            counter_p[ord(char) - ord("a")] += 1
        
        left = 0
        
        for right in range(n):
            
            # add
            counter_s[ord(s[right]) - ord("a")] += 1
            
            # is_valid
            if right - left + 1 == k:
                
                # check 
                if counter_s == counter_p:
                    result.append(left)
                
                # remove
                counter_s[ord(s[left]) - ord("a")] -= 1
                left += 1
        
        return result
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        