class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        sum = 0
        piles.sort()

        k = len(piles)//3

        for pile in range(k, len(piles), 2):

            sum += piles[pile]

        return sum
