

# link: https://leetcode.com/problems/binary-tree-level-order-traversal/


# BFS

# time: O(n)
# space: O(n)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        dq = deque([root] if root else [])
        output = []
        
        while len(dq):
            
            temp = []
            l = len(dq)
            
            for _ in range(l):
                
                parent = dq.popleft()
                if parent.left: 
                    dq.append(parent.left)
                if parent.right: 
                    dq.append(parent.right)

                temp.append(parent.val)
                
            output.append(temp)
        
        return output
            


