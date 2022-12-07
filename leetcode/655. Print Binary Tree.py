# Link: https://leetcode.com/problems/print-binary-tree/
#Q: 655. Print Binary Tree

# Time: O(N*M)
# Space: O(N*M)

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def construct(root, position, level, h):
            if not root: return
            matrix[level][position] = str(root.val)
            construct(root.left, position - 2 ** (h - level - 1), level + 1, h)
            construct(root.right, position + 2 ** (h - level - 1), level + 1, h)
            
            
        def height(root):
            if not root: return -1
            left = height(root.left)
            right = height(root.right)
            
            return 1 + max(left, right)
        
        h = height(root)
        matrix = [[""] * (2 ** (h + 1) - 1) for _ in range(h + 1)]
        row = len(matrix[0]) // 2
        construct(root, row, 0, h)
        return matrix
    

# From discuss section

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def height(root):
            return (1 + max(height(root.left), height(root.right))) if root else 0
        
        def build(root, row, left, right):
            if not root: return
            
            mid = (left + right) // 2
            matrix[row][mid] = str(root.val)
            
            build(root.left, row + 1, left, mid - 1)
            build(root.right, row + 1, mid + 1, right)
        
        h = height(root)
        width = 2 ** h - 1
        matrix = [[""] * width for _ in range(h)]
        build(root, row = 0, left = 0, right = width - 1)
        return matrix
        
        
        
        
