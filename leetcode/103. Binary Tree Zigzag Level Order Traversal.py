# link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/
# BFS

# time: O(n)
# space: O(n)

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dq = deque([root] if root else [])
        output = []
        flag = True
        
        while len(dq):
            
            temp = []
            length = len(dq)
               
            for _ in range(length):
                parent = dq.popleft()
                if parent.left:
                    dq.append(parent.left)
                if parent.right:
                    dq.append(parent.right)
                    
                temp.append(parent.val)
            
            if flag:
                output.append(temp)
                flag = False
            
            else:
                output.append(temp[::-1])
                flag = True
                
        return output
                
                
                     
