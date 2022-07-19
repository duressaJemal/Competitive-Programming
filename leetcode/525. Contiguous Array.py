# link: https://leetcode.com/problems/contiguous-array/

# time: O(n)
# space: O(n)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        count, longest = 0, 0
        dic = {0 : -1}
        
        for index, value in enumerate(nums):
            
            if value == 1:
                count += 1
            else:
                count -= 1

            if count in dic:
                longest = max(longest, index - dic[count])
            else:
                dic[count] = index
            
            
        return longest
