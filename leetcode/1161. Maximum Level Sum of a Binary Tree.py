# Link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
#Q: 1161. Maximum Level Sum of a Binary Tree

# Time: O(N)
# Space: O(N)

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([root])
        output = [root.val, 1]
        level = 0
        while queue:
            total, n = 0, len(queue)
            level += 1
            for i in range(n):
                root = queue.popleft()
                total += root.val
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                    
            if total > output[0]:
                output = [total, level]
        return output[1]
