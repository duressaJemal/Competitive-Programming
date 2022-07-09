# link: https://leetcode.com/problems/count-number-of-nice-subarrays/submissions/


# time: O(n)
# space: O(n)

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        store = {0: 1}
        total = 0
        output = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                total += 1
            if total - k in store:
                output += store[total - k]
            if total in store:
                store[total] += 1
            else:
                store[total] = 1
        return output
                
        
        
