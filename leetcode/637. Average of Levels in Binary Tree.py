# link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# time: O(n)
# space: O(n)

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque([root])
        answer = []
        
        while queue:
            
            n = len(queue)
            total = 0
            for i in range(n):
                
                p = queue.popleft()
                total += p.val
                if p.left:  queue.append(p.left)
                if p.right: queue.append(p.right)
            
            answer.append(total/n)
        
        return answer
