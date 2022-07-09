# link: https://leetcode.com/problems/subarray-sum-equals-k/submissions/

# time: O(n)
# space: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        store = {0: 1}
        total = 0
        output = 0
        n = len(nums)
        for i in range(n):
            total += nums[i]
            if total - k in store:
                output += store[total - k]
                
            if total in store:
                store[total] += 1
            else:
                store[total] = 1 
        return output
                
            
            
            
                
