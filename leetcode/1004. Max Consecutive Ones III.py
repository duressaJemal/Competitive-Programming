# link: https://leetcode.com/problems/max-consecutive-ones-iii/submissions/

# time: O(n)
# space: O(1)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        start, end, longest, zeros = 0, 0, 0, 0
        
        while end < n:
            
            if nums[end] == 0:
                zeros += 1
            
            # this makes the window valid again
            while zeros > k:
                if nums[start] == 0:
                    zeros -= 1
                start += 1
            
            longest = max(longest, end - start + 1)
            end += 1
        
        return longest
            
            
            
            
         
                
