# Link: https://leetcode.com/problems/most-frequent-subtree-sum/
#Q: 508. Most Frequent Subtree Sum

# Time: O(N)
# Space: O(N)

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        traversal = []
        
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            current_total = left + right + root.val
            traversal.append(current_total)
            return current_total
        dfs(root)
        
        counter = Counter(traversal)
        most_frequent = 1
        
        for key in counter:
            most_frequent = max(most_frequent, counter[key])
        
        output = []
        for key in counter:
            if counter[key] == most_frequent:
                output.append(key)
                
        return output
            
            
        
        
