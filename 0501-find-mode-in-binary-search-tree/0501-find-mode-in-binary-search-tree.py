# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(N)
# Space: O(N)

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        
        def dfs(root, prev, count, max_count, duplicate, output, append):
            
            if not root:
                return (prev, count)
            
            prev, count = dfs(root.left, prev, count, max_count, duplicate, output, append)
            if prev == root.val:
                count += 1
            else:
                count = 1
                prev = root.val
            
            if append:
                if count == max_count:
                    output.append(root.val)
            else:
                duplicate[0] = max(duplicate[0], count)
                
            
            prev, count = dfs(root.right, prev, count, max_count, duplicate, output, append)
            return (prev, count)

            
            
        
#         def find_count(root, prev, count, duplicate):
#             """
#             finds the count of most occuring node value
            
#             """ 
#             if not root:
#                 return (prev, count)
            
#             prev, count = find_count(root.left, prev, count, duplicate)
            
#             if prev == root.val:
#                 count += 1
#             else:
#                 count = 1
#                 prev = root.val
            
#             duplicate[0] = max(duplicate[0], count)
            
#             prev, count = find_count(root.right, prev, count, duplicate)
#             return prev, count
        
        # root, prev, count, max_count, duplicate, output, append
        duplicate = [0]
        output = []
        dfs(root, None, 0, 0, duplicate, output, append = False)
        dfs(root, None, 0, duplicate[0], duplicate, output, append = True)
        return output
        
        
            
            
            
            