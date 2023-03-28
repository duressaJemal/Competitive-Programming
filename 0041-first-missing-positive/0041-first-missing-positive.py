# Time: O(N)
# Space: O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums.append(0)
        n = len(nums)
        
        for right in range(n):
            
            # process
            while nums[right] != right:
                
                temp = nums[right]
                # skip
                if nums[right] < 0 or nums[right] >= n or nums[right] == nums[temp]:
                    break
                else:
                    nums[right], nums[temp] = nums[temp], nums[right]
            
        
        for index in range(1, len(nums)):
            if index != nums[index]:
                return index
        
        return len(nums)
            
                
        