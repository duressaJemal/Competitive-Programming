# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        output = []
        
        def dfs(node):
            
            if not node:
                output.append("*")
                return
            
            output.append(str(node.val))
            output.append("j")
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return "".join(output)
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return None
        
        self.index = 0
        def dfs():
            
            if data[self.index] == "*":
                self.index += 1
                return None
            
            # find the value
            cur = ""
            while data[self.index] != "j":
                cur += data[self.index]
                self.index += 1
            self.index += 1
            
            # create node
            node = TreeNode(int(cur))
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))