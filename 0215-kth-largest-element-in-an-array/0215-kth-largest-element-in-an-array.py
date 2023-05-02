# Time: O(N)
# Space: O(N)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = [-val for val in nums]
        heapify(heap)
        
        cur = 0
        
        while k:
            cur = heappop(heap)
            k -= 1
        
        return -cur
            