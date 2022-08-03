# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

# Sorting

# Time: O(N * log(N))
# Space: O(1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

# Heap

# Time: O(K * log(N))
# Space: O(N)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = [-num for num in nums]
        heapify(heap)
        
        while k:
            if k == 1:
                return 0 - heappop(heap)
            
            heappop(heap)
            k -=1
        
