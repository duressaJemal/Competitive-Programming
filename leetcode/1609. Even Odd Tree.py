# Link: https://leetcode.com/problems/even-odd-tree/
#Q: 1609. Even Odd Tree

# Time: O(N)
# Space: O(N)

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
        level = -1
        while queue:
            level += 1
            n, prev = len(queue), 0 if level % 2 == 0 else float("inf")
            for i in range(n):
                root = queue.popleft()
                if level % 2 == 0:
                    if root.val <= prev or root.val % 2 == 0: return False
                else:
                    if root.val >= prev or root.val % 2 != 0: return False
                    
                prev = root.val
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                
        return True
                
            
                
                
                
        
                
                
                
        
