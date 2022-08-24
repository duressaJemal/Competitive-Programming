# Link: https://leetcode.com/problems/same-tree/


# DFS

# Time: O(p + q)
# Space: O(max(p, q))

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not(p and q):
            return p == q
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

    
# BFS

# Time: O(p + q)
# Space: O(max(p, q))

    
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: return True
        
        queue = deque([p, q])
        
        while queue:
            
            left = queue.popleft()
            right = queue.popleft()
            
            if not left and not right:
                continue
                
            if not left or not right: return False
            if left.val != right.val: return False
            
            queue.append(left.left)
            queue.append(right.left)
            queue.append(left.right)
            queue.append(right.right)
            
        return True
            
            
