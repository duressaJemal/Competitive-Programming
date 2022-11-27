# Link: https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
#Q: 1104. Path In Zigzag Labelled Binary Tree

# Time: O(log(N))
# Space: O(H)

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        level = 0
        node_label = 1
        while label > node_label:
            level += 1
            node_label += 2 ** level
            
        output = [label]
        max_label, min_label = 2 ** (level + 1) - 1, 2 ** (level)
        while level > 0:
            label = (min_label + (max_label - label))//2
            output.append(label)
            max_label = min_label - 1
            min_label = min_label // 2
            level -= 1
        
        return reversed(output)
            
        
                    

