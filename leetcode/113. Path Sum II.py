# Link: https://leetcode.com/problems/path-sum-ii/
#Q: 113. Path Sum II


# Time: O(N^2) - because of the list copy()
# Space: O(H)


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        

        output = []
        
        def dfs(root, total, path):
            if not root: return
            total += root.val
            path.append(root.val)
            
            if not root.left and not root.right and total == targetSum:
                output.append(path.copy())
            
            dfs(root.left, total, path)
            dfs(root.right, total, path)
            
            path.pop()
        
        dfs(root, 0, [])
        return output
