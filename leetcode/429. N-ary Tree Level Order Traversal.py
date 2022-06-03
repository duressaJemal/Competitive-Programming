
# link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/submissions/


# Bfs
# time: O(n)
# space: O(n)

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        dq = deque([root] if root else [])
        output = []
        
        while len(dq):
            
            temp = []
            length = len(dq)
            
            for _ in range(length):
                parent = dq.popleft()
                childrens = parent.children
                
                for i in range(len(childrens)):
                    dq.append(childrens[i])
                
                temp.append(parent.val)
            
            output.append(temp)
        
        return output
                    
