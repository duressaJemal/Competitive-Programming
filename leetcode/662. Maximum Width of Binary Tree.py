# Link: https://leetcode.com/problems/maximum-width-of-binary-tree/
#Q: 662. Maximum Width of Binary Tree

# Time: O(N)
# Space: O(N)

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        mx = 1
        queue = deque([(root, 0)])
        while queue:
            mx = max(mx, queue[-1][1] - queue[0][1] + 1)
            n = len(queue)
            for i in range(n):
                root, index = queue.popleft()
                if root.left:
                    queue.append((root.left, index * 2 + 1))
                if root.right:
                    queue.append((root.right, index * 2 + 2))
            
        return mx
