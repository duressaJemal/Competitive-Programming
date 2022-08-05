# Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

# Binary search

# Time: O(M*log(N))
# Space: O(N)


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        m, n, count = len(grid), len(grid[0]), 0
        
        def binarySearch(arr, start, end, last_index):

            while start <  end:
                mid = start + (end - start) // 2
                if arr[mid] < 0:
                    end = mid
                else:
                    start = mid + 1
    
            return  last_index - start + 1

        for row in range(m):
            
            if grid[row][0] < 0:
                count += n
                continue
            if grid[row][-1] >= 0:
                continue
                
            count += binarySearch(grid[row], 0, n - 1, n - 1)
        
        return count
    
# Follow up

# Time: O(M + N)
# Space: O(1)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        row, col = m - 1, 0
        count = 0
        
        while row >= 0 and col < n:
            
            if grid[row][col] < 0:
                count += n - col
                row -= 1
            else:
                col += 1
                
        return count
            
