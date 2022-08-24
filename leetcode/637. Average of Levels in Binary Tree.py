
# Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/

# BFS

# Time: O(N)
# Space: O(N)

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        output = []
        queue = deque([root])
        
        while queue:
            
            length = len(queue)
            total = 0
            
            for _ in range(length):
                
                parent = queue.popleft()
                total += parent.val
                if parent.left:
                    queue.append(parent.left)
                if parent.right:
                    queue.append(parent.right)
                    
            output.append(total/length)
        return output


# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        dic = {}
        
        def dfs(node, level, dic):
            
            if not node:
                return
            
            if level in dic:
                dic[level] = [dic[level][0] + node.val, dic[level][1] + 1]
            else:
                dic[level] = [node.val, 1] # (node.val, number_of_nodes)
            
            dfs(node.left, level + 1, dic)
            dfs(node.right, level + 1, dic)
            
        dfs(root, 0,dic)
        
        output = []
        for key in range(len(dic)):
            output.append(dic[key][0]/dic[key][1])
        
        return output
