# Link: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
#Q: 1305. All Elements in Two Binary Search Trees

# Time: O((N+M)log(N+M))
# Space: O(N+M)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        output1 = []
        output2 = []
        
        def helper(root, output):
            if not root: return
            helper(root.left, output)
            output.append(root.val)
            helper(root.right, output)
        
        helper(root1, output1)
        helper(root2, output2)
        
        final = output1 + output2
        final.sort()
        return final

# Time: O(N+M)
# Space: O(N+M)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        output1 = []
        output2 = []
        
        def helper(root, output):
            if not root: return
            helper(root.left, output)
            output.append(root.val)
            helper(root.right, output)
        
        helper(root1, output1)
        helper(root2, output2)
        
        res = [0] * (len(output1) + len(output2))
        i, j = 0, 0
        
        # two pointer
        while i < len(output1) or j < len(output2):
            if i < len(output1) and (j == len(output2) or output1[i] <= output2[j]):
                res[i + j] = output1[i]
                i += 1
            else:
                res[i + j] = output2[j]
                j += 1
        return res
            
