# Link: https://leetcode.com/problems/diameter-of-binary-tree/

# DFS -- Brute force

# Time: O(N ^ 2)
# Space: O(N)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def diameter(node):
            
            if not node: return 0
            
            l_height = height(node.left)
            r_height = height(node.right)
            l_diameter = diameter(node.left)
            r_diameter = diameter(node.right)
        
            return max((l_height + r_height + 2), max(l_diameter, r_diameter))
            
            
        def height(node):
            
            if not node:
                return -1
            
            left = height(node.left)
            right = height(node.right)
            
            return max(left, right) + 1
        
        return diameter(root)
    
# DFS -- Optimized

# Time: O(N)
# Space: O(N)

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if not root: return -1
            left = helper(root.left)
            right = helper(root.right)
            
            # keep track of the diameter
            self.diameter = max(self.diameter, left + right + 2) 
            return 1 + max(left, right) # return height
        
        helper(root)
        return self.diameter
        

