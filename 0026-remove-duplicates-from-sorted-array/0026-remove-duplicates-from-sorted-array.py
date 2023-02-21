# Time: O(N)
# Space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        left = 0
        
        for right in range(n):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        
        return left + 1


# Time: O(Nlog(N))
# Space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 0
        
        for index in range(1, n):
            if nums[index] == nums[index - 1]:
                nums[index - 1] = 101 # out of boundary max
                count += 1
        
        nums.sort()
        return n - count
        


            
            
            
            
            
            
            