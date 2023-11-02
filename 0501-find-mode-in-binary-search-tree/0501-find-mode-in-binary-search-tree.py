# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        arr = []
        output = []
        
        def help(root):
            
            if not root:
                return 

            arr.append(root.val)
            help(root.left)
            help(root.right)
            
            return 
        
        help(root)
        counter = Counter(arr)
        mx = 0
        
        for val in counter.values():
            mx = max(mx, val)
        
        for key in counter:
            if counter[key] == mx:
                output.append(key)
        
        return output
            

            
            
                
            