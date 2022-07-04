# link: https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

# approach: Sliding Window
# time: O(n)
# space: O(n)


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        unique = set() # for storing
        start, end, longest = 0, 0, float("inf")
        n = len(cards)
        
        unique.add(cards[start])
        
        for start in range(n):
            # expanding
            while end + 1 < n and cards[end + 1] not in unique:
                end += 1
                unique.add(cards[end])
            
            # shrinking
            if end == n - 1:
                continue
                
            longest = min(longest, end - start + 2)
            unique.remove(cards[start])
        
        
        return - 1 if longest == float("inf") else longest
            
                
                
