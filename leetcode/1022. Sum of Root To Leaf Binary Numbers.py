# Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# DFS

# Time: O(N)
# Space: O(H) -- where H = height

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        def dfs(node, path):
            nonlocal total
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    total += int(path, 2)
                dfs(node.left, path)
                dfs(node.right, path)
                
        dfs(root, "")
        return total
    
# BFS

# Time: O(N)
# Space: O(N)


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        output = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node.left:
                temp = node.left.val
                node.left.val = str(node.val) + str(temp)
                queue.append(node.left)
            if node.right:
                temp = node.right.val
                node.right.val = str(node.val) + str(temp)
                queue.append(node.right)
            
            if not node.left and not node.right:
                output.append(str(node.val))
        
        total = 0
        for num in output:
            total += int(num, 2)
        
        return total
            
        
