# Link: https://leetcode.com/problems/number-of-good-pairs/
#Q: 1512. Number of Good Pairs

# Time: O(N)
# Space: O(1)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        output = 0
        counter = Counter(nums)
        for key in counter:
            n = counter[key]
            output += ((n * (n - 1)) // 2)
        
        return output
        
                 
