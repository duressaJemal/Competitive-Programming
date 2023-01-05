# # Time: O(N)
# # Space: O(N)

# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
        
#         n = len(nums)
#         ans = [0] * n
#         for index, value in  enumerate(nums):
#             ans[index] = nums[value]
        
#         return ans

# follow-up (from discuss section)

# Time: O(N)
# Space: O(1)

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        for index in range(n):
            nums[index] = nums[index] + n*(nums[nums[index]] % n)
        
        for index, value in enumerate(nums):
            nums[index] = value // n
        
        return nums