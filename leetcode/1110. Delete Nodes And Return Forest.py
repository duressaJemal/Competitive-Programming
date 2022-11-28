
# Link: https://leetcode.com/problems/delete-nodes-and-return-forest/
#Q: 1110. Delete Nodes And Return Forest

# Time: O(N)
# Space: O(H + N)

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        to_delete = set(to_delete)
        output = []
        
        def delete(root):
            if not root: return None
            root.left = delete(root.left)
            root.right = delete(root.right)
            if root.val in to_delete:
                if root.left:
                    output.append(root.left)
                if root.right:
                    output.append(root.right)
                return None
            return root
        
        val = delete(root)
        if val:
            output.append(val)
        return output
                
