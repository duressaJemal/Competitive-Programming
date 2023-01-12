# Time: O(N), where N = total number of characters
# Space: O(1)

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        row_length = len(strs)
        column_length = len(strs[0])
        
        unsorted_column_count = 0
        
        for col in range(column_length):
            prev = ""
            for row in range(row_length):
                if strs[row][col] >= prev:
                    prev = strs[row][col]
                else:
                    unsorted_column_count += 1
                    break
        
        return unsorted_column_count
        
        
        
        
        
                
                
        