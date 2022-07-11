# https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        
        heappush(self.heap, val)
        while len(self.heap) > self.k:
            heappop(self.heap)
            
        return self.heap[0]
