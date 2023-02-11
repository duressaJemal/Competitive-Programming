class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        banned = set(banned)
        total = 0
        count = 0
        
        for i in range(1, n + 1):
            if i not in banned:
                if total + i <= maxSum:
                    count += 1
                    total += i
                else:
                    break
        
        return count
                
                
        