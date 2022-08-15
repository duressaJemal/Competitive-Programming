
# Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# DFS + BFS

# Time: O(N)
# Space: O(N)

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(node, parent):
            
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root, None)
        
        queue = collections.deque([target])
        visited = set()
        
        for _ in range(k):
            length = len(queue)
            
            for _ in range(length): # for keeping track of the levels
                current_node = queue.popleft()
                visited.add(current_node)
                
                for node in [current_node.left, current_node.right, current_node.parent]:
                    if node and node not in visited:
                        queue.append(node)
        
        return [node.val for node in queue]
            
