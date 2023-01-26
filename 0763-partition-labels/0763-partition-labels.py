# Time: O(N)
# Space: O(N)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        n = len(s)
        output = []
        
        last_index = defaultdict(int)
        for index, value in enumerate(s):
            last_index[value] = index
        
        max_index = 0
        left = 0
        
        for index in range(n):
            max_index = max(max_index, last_index[s[index]])
            if index == max_index:
                output.append(index - left + 1)
                left = index + 1
            
        return output
                