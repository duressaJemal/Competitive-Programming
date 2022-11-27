# Link: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
#Q: 865. Smallest Subtree with all the Deepest Nodes

# Time: O(N)
# Space: O(H)

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def helper(root):
            if not root: return (None, -1)
            
            left = helper(root.left)
            right = helper(root.right)
            
            if left[1] == right[1]:
                return (root, left[1] + 1)
            else:
                # compare
                if left[1] > right[1]:
                    return (left[0], left[1] + 1)
                else:
                    return (right[0], right[1] + 1)
            
        return helper(root)[0]
