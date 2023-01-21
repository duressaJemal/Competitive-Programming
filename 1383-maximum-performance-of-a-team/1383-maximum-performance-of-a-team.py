class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        heap = []
        result = 0
        total = 0
        
        for x, min_eff in sorted(list(zip(speed, efficiency)), key=lambda arr: -arr[1]):
            
            total += x
            heappush(heap, x)
            
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) <= k:
                result = max(result, min_eff * total)
        
        return result % (10 ** 9 + 7)
            
        