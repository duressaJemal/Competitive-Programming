class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        n = len(self.w)
        for index in range(1, n):
            self.w[index] += self.w[index - 1]

    def pickIndex(self) -> int:
        
        n = len(self.w)
        target = random.randint(1, self.w[-1])
        
        left = -1
        right = n - 1 # always valid
        
        while right > left + 1:
            mid = (left + right) // 2
            
            if target > self.w[mid]:
                left = mid
            elif target < self.w[mid]:
                right = mid
            else:
                return mid
      
        return right
                
                
        

        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()