# Link: https://leetcode.com/problems/deepest-leaves-sum/
#Q: 1302. Deepest Leaves Sum

# Time: O(N)
# Space: O(N)

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        self.output = 0
        def height(root):
            if not root: return -1
            return max(height(root.left), height(root.right)) + 1
        
        
        def helper(root, height):
            if not root: return
            if not height:
                self.output += root.val
                return
            helper(root.left, height - 1)
            helper(root.right, height - 1)
        
        h = height(root)
        helper(root, h)
        return self.output
