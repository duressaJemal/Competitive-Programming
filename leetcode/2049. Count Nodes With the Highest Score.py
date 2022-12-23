# Link: https://leetcode.com/problems/count-nodes-with-the-highest-score/
#Q: 2049. Count Nodes With the Highest Score

# Time: O(N)
# Space: O(H) 

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        
        def postorder(node, max_size):
            left = 0
            right = 0
            
            if len(tree[node]):
                left = postorder(tree[node][0], max_size)
            if len(tree[node]) > 1:
                right = postorder(tree[node][1], max_size)
            
            # calculate the max score for the current node
            
            above = max((n - left - right - 1) , 1)
            left_subtree = max(left, 1)
            right_subtree = max(right, 1)
            score = above * left_subtree * right_subtree

            if score > max_size[0][0]:
                max_size[0] = [score, 1]
            elif score == max_size[0][0]:
                # increase the count of current highest score
                max_size[0][1] += 1
            
            return left + right + 1
        
        n = len(parents)
        max_size = [[0, 0]] # (max_value, count)
        tree = {}
        
        for i in range(n):
            tree[i] = []
        
        for index, value in enumerate(parents):
            if value != -1:
                tree[value].append(index)
                
        postorder(0, max_size)
        
        return max_size[0][1]
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
