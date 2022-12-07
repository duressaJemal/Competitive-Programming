# Link: https://leetcode.com/problems/complete-binary-tree-inserter/
#Q: 919. Complete Binary Tree Inserter

class CBTInserter:

    # Time: O(N)
    # Space: O(1)
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.deque = deque([])
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
       
    # Time: O(1)
    def insert(self, val: int) -> int:
        
        node = self.deque[0]
        new_node = TreeNode(val)
        self.deque.append(new_node)
        
        if not node.left:
            node.left = new_node
        elif not node.right:
            node.right = new_node
            self.deque.popleft()
        
        return node.val
        
    # Time: O(1)
    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
