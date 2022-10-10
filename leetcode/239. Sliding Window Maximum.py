# Link: https://leetcode.com/problems/sliding-window-maximum/submissions/
#Q: 239. Sliding Window Maximum

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
        
