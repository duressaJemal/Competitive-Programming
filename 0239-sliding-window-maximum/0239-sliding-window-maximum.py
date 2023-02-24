# Time: O(N)
# Space: O(M) where, M = (N - k)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        
        max_queue = deque([])
        output = []
        
        def add(val):
    
            while max_queue and max_queue[-1] < val:
                max_queue.pop()
            max_queue.append(val)
        
        def remove(index):
            curr = nums[index]
            
            if max_queue and max_queue[0] == curr:
                max_queue.popleft()
            
        def good(l, r):
            return r - l + 1 == k
        
        left = 0
        right = 0
        
        while right < n:
            # add
            add(nums[right])

            # validate
            while not good(left, right):
                right += 1
                add(nums[right])
                
            # record
            if good(left, right):
                output.append(max_queue[0])
                
            # remove
            remove(left)
            left += 1
            right += 1
        
        return output
            

# Time: O(N) -- N = max(len(nums) / k  + 2 * len(nums))
# space: O(k)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n, l, res, output = len(nums), 0, 0, []
        s1, s2, = [], []
        max_s1, max_s2 = [float("-inf")], [float("-inf")]
        
        def add(x):
            s2.append(x)
            max_s2.append(max(max_s2[-1], s2[-1]))

            
        def remove():
            if not s1:
                while s2:
                    s1.append(s2.pop())
                    max_s2.pop()
                    max_s1.append(max(max_s1[-1], s1[-1]))
            
            s1.pop()
            max_s1.pop()
            
        def good(l, r):
            return r - l + 1 == k
            
        r = 0
        while r < n:
            add(nums[r])
            while not good(l, r):
                r += 1
                add(nums[r])
            
            res = max(max_s1[-1], max_s2[-1])
            output.append(res)
            remove()
            l += 1
            r += 1
        
        return output

    

            
            

        
        
        