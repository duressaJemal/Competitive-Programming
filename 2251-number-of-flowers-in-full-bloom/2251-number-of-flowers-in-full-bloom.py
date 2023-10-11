# Time: O(Nlog(N))
# Space: O(N)

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        n = len(flowers)
        
        s_first = sorted([a[0] for a in flowers])
        s_second = sorted([a[1] for a in flowers])
        
        output = []
        
        for target in people:
            
            left_len = bisect.bisect_right(s_second, target - 1)
            right_len = bisect.bisect_left(s_first, target + 1)
            
            output.append(n - (left_len + (n - right_len)))
        
        return output
            
            
            
            