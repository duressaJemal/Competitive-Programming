# Link: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
#Q: 1457. Pseudo-Palindromic Paths in a Binary Tree

# Time: O(N)
# Space: O(H + K) 

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        count = Counter()
        
        def helper(root):
            if not root: 
                return 0
            count[root.val] += 1
            
            if not root.left and not root.right:
                odds_len = 0
                for k in count:
                    if count[k] % 2 != 0: 
                        odds_len += 1
                        if odds_len > 1:
                            count[root.val] -= 1
                            return 0
                count[root.val] -= 1
                return 1
            
            value = helper(root.right) + helper(root.left)
            count[root.val] -=1
            return value
            
        return helper(root)
            
