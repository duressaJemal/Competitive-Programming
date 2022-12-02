
# Link: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
#Q: 1530. Number of Good Leaf Nodes Pairs

# Time: O(N)
# Space: O(N)

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        
        self.output = 0
        
        def dfs(root):
            if not root: return []
            if not root.right and not root.left: 
                return [1]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            for i in range(len(left)):
                for j in range(len(right)):
                    if left[i] + right[j] <= distance:
                        self.output += 1
            
            current = left + right
            for i in range(len(current)):
                current[i] += 1
            
            return current
    
        dfs(root)
        return self.output
                    
