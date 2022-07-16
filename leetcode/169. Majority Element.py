# link: https://leetcode.com/problems/majority-element/submissions/

# Sorting

# time: O(nlog(n))
# space: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()
        return nums[len(nums)//2]
            

        
# Boyer-Moore Voting Algorithm

# time: O(n)
# space: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority = None
        count = 0
        
        for num in nums: 
            
            if count == 0:
                majority = num
            
            count += (1 if num == majority else -1)
            
        return majority
            
            
            
