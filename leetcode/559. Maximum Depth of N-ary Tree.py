# link: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

# DFS

# time: O(n)
# space: O(n)

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        
        if not root:
            return 0
        
        def dfs(root):
            
            if root.children == None:
                return 1
            
            depth = 0
            for children in root.children:
                depth = max(depth, dfs(children))
                
            return depth + 1

        return dfs(root)

# BFS

# time: O(n)
# space: O(n)

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        depth = 0
        queue = deque([root])
        current_level_nodes = 1
        next_level_nodes = 0

        if not root:
            return 0

        while queue:

            parent = queue.popleft()
            current_level_nodes -= 1

            for child in parent.children:
                queue.append(child)
                next_level_nodes += 1

            if current_level_nodes == 0:
                depth += 1
                current_level_nodes = next_level_nodes
                next_level_nodes = 0

        return depth

