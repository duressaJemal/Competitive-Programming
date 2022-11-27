# Link: https://leetcode.com/problems/smallest-string-starting-from-leaf/
#Q: 988. Smallest String Starting From Leaf

# Time: O(N*Log(N))
# Space: O(N)

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.output = "{"
        
        def helper(root, path):
            if not root: return
            path.append(chr(root.val + ord("a")))
            if not root.left and not root.right:
                self.output = min(self.output, "".join(reversed(path)))
            helper(root.left, path)
            helper(root.right, path)
            path.pop()
            
        helper(root, [])
        return self.output
