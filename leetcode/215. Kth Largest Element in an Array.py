# link: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

# sorting

# time: O(nlogn)
# space: O(n)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

# heap

# time: O(n)
# space: O(n)

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        while k:
            if k == 1:
                return 0 - heapq.heappop(heap)
            
            heapq.heappop(heap)
            k -=1
        
        
        
