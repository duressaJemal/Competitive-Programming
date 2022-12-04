# Link: https://leetcode.com/problems/validate-binary-tree-nodes/
#Q: 1361. Validate Binary Tree Nodes

# Time: O(N)
# Space: O(N)

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        # Find persumed root
        childrenNodes = set(leftChild + rightChild)
        
        root = 0
        for i in range(n):
            if i not in childrenNodes:
                root = i
                break
        
        def dfs(index, depth):
            if index in visited:
                self.unique = False
                return
            
            if index == -1 or depth == n: return
            visited.add(index)
            dfs(leftChild[index], depth + 1)
            dfs(rightChild[index], depth + 1)
          
        self.unique = True
        visited = set()
        dfs(root, 0)
        
        # The presumed root is the only root.
        if len(visited) == n:
            return self.unique
        # There is another root, not only one binary tree
        else:
            return False
        
        
# From discuss section

# Time: O(N)
# Space: O(N)

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        # Find root
        childrenNodes = set(leftChild + rightChild)
        root = 0
        for i in range(n):
            if i not in childrenNodes:
                root = i
                break
                
        # traverse
        queue = deque([root])
        visited = set()
        
        while queue:
            root = queue.popleft()
            if root in visited:
                return False
            
            visited.add(root)
            
            if leftChild[root] != -1:
                queue.append(leftChild[root])
            if rightChild[root] != -1:
                queue.append(rightChild[root])
            
        return len(visited) == n
