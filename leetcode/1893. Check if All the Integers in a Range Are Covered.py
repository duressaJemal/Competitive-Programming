# Link: https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
#Q: 1893. Check if All the Integers in a Range Are Covered

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        all_values = set()
        for left_bound, right_bound in ranges:
            for x in range(left_bound, right_bound + 1):
                all_values.add(x)
        
        for value in range(left, right + 1):
            if value not in all_values:
                return False
            
        return True

# Sweep line from discuss section

# Time: O(N + R) where R = range[left, right]
# Space: O(N)

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        
        range_sum = defaultdict(int)
        for left_bound, right_bound in ranges:
            range_sum[left_bound] += 1
            range_sum[right_bound + 1] -= 1
        
        total = 0
        for i in range(right + 1):
            total += range_sum[i]
            if i >= left and total == 0:
                return False
        
        return True
        
        
        
        
        
        
