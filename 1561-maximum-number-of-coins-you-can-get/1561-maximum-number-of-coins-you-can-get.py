class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        n = len(piles)
        
        max_coins = 0
        piles.sort()
        
        for index in range(n // 3, n, 2):
            max_coins += piles[index]
        
        return max_coins