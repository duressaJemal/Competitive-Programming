# link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/submissions/

# time: O(n)
# space: O(1)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        
        if k == n:
            return sum(cardPoints)
        
        left, right = 0, n - k - 1
        total = sum(cardPoints[:n - k])
        minimum = total
        
        while right < n:
        
            total -= cardPoints[left]
            left += 1
            
            if right == n - 1:
                break
            
            right += 1
            total += cardPoints[right]
            minimum = min(minimum, total)
        
        total = sum(cardPoints)
        
        return total - minimum
            
