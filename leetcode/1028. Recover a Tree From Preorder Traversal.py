
# Link: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
#Q: 1028. Recover a Tree From Preorder Traversal

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        self.current_index = 0
        
        def build(depth):
            if self.current_index >= len(traversal): return None
            
            index = self.current_index
            count = 0
            
            while traversal[index] == "-":
                count += 1
                index += 1
            
            start = index
            while index < len(traversal) and traversal[index] != "-":
                index += 1
            
            if count == depth:
                node = TreeNode(int(traversal[start:index]))
                self.current_index = index
            else:
                return None
            
            
            node.left = build(depth + 1)
            node.right = build(depth + 1)
            
            return node
        
        return build(0)

# From discuss section

# Time: O(S)
# Space: O(N)

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        stack, i = [], 0
        
        while i < len(traversal):
            level, val = 0, ""
            while i < len(traversal) and traversal[i] == "-":
                level += 1
                i += 1
            
            while i < len(traversal) and traversal[i] != "-":
                val += traversal[i]
                i += 1
            
            node = TreeNode(int(val))
            
            while len(stack) > level:
                stack.pop()
            
            if stack and stack[-1].left == None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            
            stack.append(node)
        
        return stack[0]
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
        
        
        
        
        
        
        
        
