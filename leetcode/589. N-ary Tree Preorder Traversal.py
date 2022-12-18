# Link: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
#Q: 589. N-ary Tree Preorder Traversal

# Time: O(N)
# Space: O(N)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        def preorder(root):
            if not root: return None
            output.append(root.val)
            for child in root.children:
                preorder(child)
        preorder(root)
        return output

# Time: O(N)
# Space: O(N)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        output = []
        stack = [root]
        
        while stack and root:
            root = stack.pop()
            output.append(root.val)
            
            for child in reversed(root.children):
                stack.append(child)
        
        return output
