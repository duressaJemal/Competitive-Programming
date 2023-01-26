class Solution:
    def partitionString(self, s: str) -> int:
        
        """
        the best approach to minimize the length is to maximize 
        each partition
        
        make each partition a set
        then if the arr[r] not in set:
            add
        else:
            increment left and right
        
        """
        
        n = len(s)
        unique = set()
        count = 1
        
        for right in range(n):
            if s[right] in unique:
                count += 1
                unique = set()
                unique.add(s[right])
            else:
                unique.add(s[right])
        
        return count
                
            
            
        
        