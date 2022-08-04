# Link: https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        
    # Time: O(logN)
    # Space: O(N)
    
    def addNum(self, num: int) -> None:
        
        if not self.small or -self.small[0] >= num:
            heappush(self.small, -num) 
        else:
            heappush(self.large, num)
            
        # Balancing
        
        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -heappop(self.small))
        if len(self.small) < len(self.large):
            heappush(self.small, -heappop(self.large))
 
    # Time: O(1)
    # Space: O(1)
    
    def findMedian(self) -> float:
    
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0])/2
        else:
            return -self.small[0]
        
