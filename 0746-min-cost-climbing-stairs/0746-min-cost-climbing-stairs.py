class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        
        one = cost[0]
        two = cost[1]
        
        for i in range(2, n + 1):
            cur = min(one, two) + (cost[i] if i < n else 0)
            one, two = two, cur
        
        return two