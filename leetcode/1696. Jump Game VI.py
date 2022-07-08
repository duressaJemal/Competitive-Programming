# link: https://leetcode.com/problems/jump-game-vi/submissions/

from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        max_q = deque([(nums[0], 0)])
        
        for i in range(1, len(nums)):
            score = max_q[0][0] + nums[i]
            while max_q and max_q[-1][0] < score:
                max_q.pop()
                
            max_q.append((score, i))
            if max_q[0][1] == i- k:
                max_q.popleft()
            
        return max_q[-1][0]
        
