# Time: O(N)
# Space: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        return (n * (n + 1)) // 2 - sum(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.append("x")
        n = len(nums)
        
        for cur in range(n):
            while nums[cur] != "x" and nums[cur] != cur:
                temp = nums[cur]
                nums[cur] = nums[nums[cur]]
                nums[temp] = temp
        
        for index in range(len(nums)):
            if nums[index] == "x":
                return index
                
        
                
                