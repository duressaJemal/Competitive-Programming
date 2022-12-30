# Link: https://leetcode.com/problems/sum-of-even-numbers-after-queries/
#Q: 985. Sum of Even Numbers After Queries

# Time: O(N + M) where M = size of qeuries
# Space: O(M) 

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        n = len(nums)
        output = []
        
        total_even = 0
        
        for num in nums:
            if num % 2 == 0:
                total_even += num

        for value, index in queries:
            
            if nums[index] % 2 == 0:
                total_even -= nums[index]
            
            nums[index] += value
            if nums[index] % 2 == 0:
                total_even += nums[index]

            output.append(total_even)
        
        return output
