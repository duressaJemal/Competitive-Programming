# Link: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
#Q: 515. Find Largest Value in Each Tree Row

# Time: O(N)
# Space: O(N)

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        queue = deque([root]) if root else []
        while queue:
            n, largest = len(queue), float("-inf")
            for _ in range(n):
                root = queue.popleft()
                largest = max(largest, root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            
            output.append(largest)
        return output

# Time: O(N)
# Space: O(H)

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
        def helper(root, level):
            if not root: return
            if level == len(output):
                output.append(float("-inf"))
            
            output[level] = max(output[level], root.val)
            helper(root.left, level + 1)
            helper(root.right, level + 1)
        helper(root, 0)
        return output
        
        
