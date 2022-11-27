# Link: https://leetcode.com/problems/leaf-similar-trees/
#Q: 872. Leaf-Similar Trees

# Time: O(N1 + N2)
# Space: O(N1 + N2)

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        output1 = []
        output2 = []
        
        def helper(root, output):
            if not root: return
            if not root.left and not root.right:
                output.append(root.val)
            helper(root.left, output)
            helper(root.right, output)
        
        helper(root1, output1)
        helper(root2, output2)
        return output1 == output2
