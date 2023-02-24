# Time: O(N)
# Space: O(N)

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        n = len(nums)
        max_length = 0
        
        max_queue = deque([])
        min_queue = deque([])
        
        # add
        def add(val):
            
            # max_queue
            while max_queue and max_queue[-1] < val:
                max_queue.pop()
            
            # min_queue
            while min_queue and min_queue[-1] > val:
                min_queue.pop()
                
            max_queue.append(val)
            min_queue.append(val)
        
        def remove(index):
            
            curr = nums[index]
            
            if min_queue and min_queue[0] == curr:
                min_queue.popleft()
            
            if max_queue and max_queue[0] == curr:
                max_queue.popleft()
            
        
        def good():
            return (max_queue[0] - min_queue[0]) <= limit
        
        
        left = 0
        for right in range(n):
            # add
            add(nums[right])
            
            # validate
            while not good():
                remove(left)
                left += 1
         
            # record
            max_length = max(max_length, right - left + 1)
        
        return max_length
                
            
            
            
        
            
        
        