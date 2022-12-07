# Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
#Q: 653. Two Sum IV - Input is a BST

# Time: O(Nlog(N))
# Space: O(H)

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def dfs(node):
            if not node: return False
            return find_value(root, k - node.val) or dfs(node.left) or dfs(node.right)
        
        
        def find_value(root, target):
            if not root: return False
            if root.val == target and target * 2 != k: return True
            if root.val > target:
                return find_value(root.left, target)
            return find_value(root.right, target)
        
        return dfs(root)
    
# Time: O(N)
# Space: O(N)

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorder(root):
            if not root: return
            inorder(root.left)
            traversal.append(root.val)
            inorder(root.right)
        
        traversal = []
        inorder(root)
        
        l, r = 0, len(traversal) - 1
        while l < r:
            value = traversal[l] + traversal[r]
            if value == k: return True
            if value < k:
                l += 1
                continue
            else:
                r -= 1
                continue
        return False
 
