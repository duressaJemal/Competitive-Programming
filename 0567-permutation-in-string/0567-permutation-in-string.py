# Time: O(N)
# Space: O(k) where k = 26, O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k = len(s1)
        n = len(s2)
        
        counter_s1 = Counter(s1)
        counter_s2 = Counter()
        
        left = 0
        
        for right in range(n):
            
            # add
            counter_s2[s2[right]] += 1
            
            # validate
            if right - left + 1 == k:
                
                # check
                if counter_s1 == counter_s2:
                    return True
                
                # remove
                counter_s2[s2[left]] -= 1
                left += 1
        
        return False
            
        