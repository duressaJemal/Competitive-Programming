# link: https://leetcode.com/problems/minimum-increment-to-make-array-unique/submissions/

# time: O(nlog(n))
# space: O(n)

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        n = len(nums)
        start, addition = 0, 0
        unique = set()
        
        nums.sort()
        while start < n:

            if nums[start] in unique:
                difference = (nums[start - 1] + 1) - nums[start]
                nums[start] += difference
                addition += difference
            unique.add(nums[start])
            start += 1
            
        return addition
                
        
