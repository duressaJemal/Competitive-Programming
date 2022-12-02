# Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
#Q: 108. Convert Sorted Array to Binary Search Tree

# Time: O(N)
# Space: O(N)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(left_index, right_index):
            
            if left_index > right_index: return None
            if left_index == right_index: return TreeNode(nums[left_index])
            
            current_index = left_index + (right_index - left_index) // 2
            node = TreeNode(nums[current_index])
            
            node.left = dfs(left_index, current_index - 1)
            node.right = dfs(current_index + 1, right_index)
            
            return node
        
        return dfs(0, len(nums) - 1)
        
