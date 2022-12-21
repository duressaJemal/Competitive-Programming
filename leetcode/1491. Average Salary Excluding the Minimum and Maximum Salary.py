# Link: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
#Q: 1491. Average Salary Excluding the Minimum and Maximum Salary

# Time: O(N)
# Space: O(1)

class Solution:
    def average(self, salary: List[int]) -> float:
        
        mn = float("inf")
        mx = float("-inf")
        
        for num in salary:
            mn = min(mn, num)
            mx = max(mx, num)
        
        return (sum(salary) - mn - mx) / (len(salary) - 2)
