# link: https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:
    
    # time: O(n)
    # space: O(n)
    
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapify(self.heap)
        self.k = k

    # time: O((n - k) + log(n))
    # space: O(n)
    
    def add(self, val: int) -> int:
        
        heappush(self.heap, val)
        
        while len(self.heap) > self.k:
            heappop(self.heap)
            
        return self.heap[0]
